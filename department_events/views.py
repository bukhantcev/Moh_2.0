from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DepartmentEvent, DepartmentEventType, DepartmentEventName, DepartmentEventLocation
from accounts.models import Profile
from .forms import DepartmentEventForm
from django import forms
import datetime
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class EventTypeForm(forms.ModelForm):
    class Meta:
        model = DepartmentEventType
        fields = ['name']

class EventNameForm(forms.ModelForm):
    class Meta:
        model = DepartmentEventName
        fields = ['name']

@login_required
def create_department_event(request):
    if request.user.profile.dolgnost.name != "Начальник подразделения":
        return redirect('/')

    if request.method == 'POST':
        date = request.POST.get('date')
        type_id = request.POST.get('type')
        name_id = request.POST.get('name')
        location_id = request.POST.get('location')
        description = request.POST.get('description', '')
        selected_ids = request.POST.getlist('employees')

        event = DepartmentEvent.objects.create(
            datetime=date,
            department=request.user.profile.podrazdelenie,
            type_id=type_id,
            name_id=name_id,
            location_id=location_id,
            description=description
        )
        event.staff.set(Profile.objects.filter(id__in=selected_ids))

        scroll_to = date[:10]
        return redirect(f"/?scroll_to={scroll_to}")

    copy_id = request.GET.get('copy_id')
    if copy_id:
        try:
            original = DepartmentEvent.objects.get(id=copy_id)
            context = {
                'date': original.datetime.strftime('%Y-%m-%dT%H:%M'),
                'types': DepartmentEventType.objects.filter(department=request.user.profile.podrazdelenie),
                'names': DepartmentEventName.objects.filter(department=request.user.profile.podrazdelenie),
                'locations': DepartmentEventLocation.objects.filter(department=request.user.profile.podrazdelenie),
                'users': Profile.objects.filter(podrazdelenie=request.user.profile.podrazdelenie),
                'selected_type': original.type.id,
                'selected_name': original.name.id,
                'selected_location': original.location.id,
                'description': original.description,
                'selected_employees': original.staff.values_list('id', flat=True),
            }
            return render(request, 'department_events/create_event.html', context)
        except DepartmentEvent.DoesNotExist:
            pass

    date = request.GET.get('date')
    if date:
        date += 'T19:00'

    context = {
        'date': date,
        'types': DepartmentEventType.objects.filter(department=request.user.profile.podrazdelenie),
        'names': DepartmentEventName.objects.filter(department=request.user.profile.podrazdelenie),
        'locations': DepartmentEventLocation.objects.filter(department=request.user.profile.podrazdelenie),
        'users': Profile.objects.filter(podrazdelenie=request.user.profile.podrazdelenie),
    }
    return render(request, 'department_events/create_event.html', context)

def edit_dep_event(request, event_id):
    event = get_object_or_404(DepartmentEvent, id=event_id)
    if request.method == 'POST':
        event.datetime = datetime.datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
        event.type_id = request.POST.get('type')
        event.name_id = request.POST.get('name')
        event.location_id = request.POST.get('location')
        event.description = request.POST.get('description', '')
        event.save()
        selected_ids = request.POST.getlist('employees')
        event.staff.set(Profile.objects.filter(id__in=selected_ids))
        scroll_to = event.datetime.strftime('%Y-%m-%d')
        return redirect(f"/?scroll_to={scroll_to}")

    context = {
        'event': event,
        'date': event.datetime.strftime('%Y-%m-%dT%H:%M'),
        'types': DepartmentEventType.objects.filter(department=event.department),
        'names': DepartmentEventName.objects.filter(department=event.department),
        'locations': DepartmentEventLocation.objects.filter(department=event.department),
        'users': Profile.objects.filter(podrazdelenie=event.department),
        'selected_employees': event.staff.values_list('id', flat=True)
    }
    return render(request, 'department_events/edit_dep_event.html', context)

def delete_dep_event(request, event_id):
    event = get_object_or_404(DepartmentEvent, id=event_id)
    scroll_to = event.datetime.date()
    event.delete()
    return redirect(f"/?scroll_to={scroll_to}")

@csrf_exempt
def update_dep_event_date(request, event_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_date_str = data.get('date')
            is_copy = data.get('copy') == True or data.get('copy') == 'true'

            if not new_date_str:
                return JsonResponse({'error': 'No date provided'}, status=400)

            original_event = get_object_or_404(DepartmentEvent, id=event_id)

            old_time = original_event.datetime.time()
            new_date = datetime.datetime.strptime(new_date_str, '%Y-%m-%d').date()
            new_datetime = datetime.datetime.combine(new_date, old_time)

            if is_copy:
                copied_event = DepartmentEvent.objects.create(
                    datetime=new_datetime,
                    type=original_event.type,
                    name=original_event.name,
                    location=original_event.location,
                    description=original_event.description,
                    department=original_event.department
                )
                copied_event.staff.set(original_event.staff.all())
                return JsonResponse({'status': 'ok', 'copied': True})
            else:
                original_event.datetime = new_datetime
                original_event.save()
                return JsonResponse({'status': 'ok', 'copied': False})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_type(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj = DepartmentEventType.objects.create(
                name=data['name'],
                department=request.user.profile.podrazdelenie
            )
            return JsonResponse({'id': obj.id, 'name': obj.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_name(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj = DepartmentEventName.objects.create(
                name=data['name'],
                department=request.user.profile.podrazdelenie
            )
            return JsonResponse({'id': obj.id, 'name': obj.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_location(request):
    print('ok')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj = DepartmentEventLocation.objects.create(
                name=data['name'],
                department=request.user.profile.podrazdelenie
            )
            return JsonResponse({'id': obj.id, 'name': obj.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@login_required
def manage_dep_event_types(request):
    event_types = DepartmentEventType.objects.filter(department=request.user.profile.podrazdelenie)
    return render(request, 'department_events/manage_dep_event_types.html', {'event_types': event_types})

@login_required
def manage_dep_event_names(request):
    event_names = DepartmentEventName.objects.filter(department=request.user.profile.podrazdelenie)
    return render(request, 'department_events/manage_dep_event_names.html', {'event_names': event_names})

@login_required
def manage_dep_event_locations(request):
    event_locations = DepartmentEventLocation.objects.filter(department=request.user.profile.podrazdelenie)
    return render(request, 'department_events/manage_dep_event_locations.html', {'event_locations': event_locations})

@login_required
def edit_dep_event_type(request, pk):
    instance = get_object_or_404(DepartmentEventType, pk=pk, department=request.user.profile.podrazdelenie)
    if request.method == 'POST':
        form = EventTypeForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_types')
    else:
        form = EventTypeForm(instance=instance)
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Редактировать тип события'})

@login_required
def edit_dep_event_name(request, pk):
    instance = get_object_or_404(DepartmentEventName, pk=pk, department=request.user.profile.podrazdelenie)
    if request.method == 'POST':
        form = EventNameForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_names')
    else:
        form = EventNameForm(instance=instance)
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Редактировать название события'})

class EventLocationForm(forms.ModelForm):
    class Meta:
        model = DepartmentEventLocation
        fields = ['name']
@login_required
def edit_dep_event_location(request, pk):
    instance = get_object_or_404(DepartmentEventLocation, pk=pk, department=request.user.profile.podrazdelenie)
    if request.method == 'POST':
        form = EventLocationForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_locations')
    else:
        form = EventLocationForm(instance=instance)
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Редактировать место проведения'})

@login_required
def delete_dep_event_location(request, pk):
    instance = get_object_or_404(DepartmentEventLocation, pk=pk, department=request.user.profile.podrazdelenie)
    instance.delete()
    return redirect('manage_dep_event_locations')

@login_required
def delete_dep_event_name(request, pk):
    instance = get_object_or_404(DepartmentEventName, pk=pk, department=request.user.profile.podrazdelenie)
    instance.delete()
    return redirect('manage_dep_event_names')

@login_required
def delete_dep_event_type(request, pk):
    instance = get_object_or_404(DepartmentEventType, pk=pk, department=request.user.profile.podrazdelenie)
    instance.delete()
    return redirect('manage_dep_event_types')

@login_required
def create_dep_event_name(request):
    if request.method == 'POST':
        form = EventNameForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_names')
    else:
        form = EventNameForm()
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Новое название мероприятия'})

@login_required
def create_dep_event_location(request):
    if request.method == 'POST':
        form = EventLocationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_locations')
    else:
        form = EventLocationForm()
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Новое место проведения'})

def create_dep_event_type(request):
    if request.method == 'POST':
        form = EventTypeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = request.user.profile.podrazdelenie
            instance.save()
            return redirect('manage_dep_event_types')
    else:
        form = EventTypeForm()
    return render(request, 'department_events/simple_form.html', {'form': form, 'title': 'Новый тип мероприятия'})
