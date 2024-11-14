from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
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

    context = {
        'users': users_list
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