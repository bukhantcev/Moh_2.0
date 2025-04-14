from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from accounts.forms import FormValid

from accounts.models import Profile

from accounts.models import Podrazdelenie, Dolgnost


# Create your views here.
def index(request):#--------------------------------------------ROOM
    users = User.objects.all()
    users_list = []
    for user in users:
        if not user.groups.filter(name='podtvergdennie').exists():
            users_list.append(user)

    podrazdelenie_list = Podrazdelenie.objects.all()
    dolgnost_list = Dolgnost.objects.all()

    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)

        # Обновление профиля
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.save()

        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.phone = request.POST.get('phone')
        profile.podrazdelenie = Podrazdelenie.objects.get(id=request.POST.get('podrazdelenie'))
        profile.dolgnost = Dolgnost.objects.get(id=request.POST.get('dolgnost'))
        profile.save()

        # Смена пароля, только если введены соответствующие поля
        if request.POST.get('old_password') or request.POST.get('new_password1') or request.POST.get('new_password2'):
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')

            if not old_password or not new_password1 or not new_password2:
                messages.error(request, 'Пожалуйста, заполните все поля для смены пароля.')
            elif new_password1 != new_password2:
                messages.error(request, 'Новые пароли не совпадают.')
            elif not request.user.check_password(old_password):
                messages.error(request, 'Старый пароль введён неверно.')
            else:
                request.user.set_password(new_password1)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Пароль успешно изменён.')
        else:
            messages.success(request, 'Данные профиля сохранены.')

        return redirect('room')

    context = {
        'users': users_list,
        'podrazdelenie_list': podrazdelenie_list,
        'dolgnost_list': dolgnost_list
    }
    return render(request, 'room/index.html', context=context)


def form_valid(request):
    if request.method == 'GET':
        if 'user_id' in request.GET:
            user = Profile.objects.get(user=User.objects.get(id=request.GET.get('user_id')))
            form = FormValid(instance=user)
            context = {
                'user': user,
                'form': form,
            }
            return render(request, 'room/form_valid.html', context=context)
    if request.method == 'POST':
        print(request.POST)
        if 'podtverdit' in request.POST:
            user = Profile.objects.get(id=request.POST.get('podtverdit'))
            user.phone = request.POST.get('phone')
            user.podrazdelenie = Podrazdelenie.objects.get(id=request.POST.get('podrazdelenie'))
            user.dolgnost = Dolgnost.objects.get(id=request.POST.get('dolgnost'))
            user.save()
            user = User.objects.get(username=Profile.objects.get(id=request.POST.get('podtverdit')).user)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            g = Group.objects.get(name='podtvergdennie')

            user.groups.add(g)
            user.save()

            return redirect('/room')
        if 'delete' in request.POST:

            user = User.objects.get(username=Profile.objects.get(id=request.POST.get('delete')).user)
            user.delete()

            return redirect('/room')
    context = {
        'user': 'Ошибка'
    }
    return render(request, 'room/form_valid.html', context=context)