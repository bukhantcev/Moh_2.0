import datetime
import os
import shutil
from cProfile import label
from lib2to3.fixes.fix_input import context

from dateutil.utils import today
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import calendar, calendar_switch_month, my_calendar, calendar_switch_year, autoscroll, Spect
from forms.models import Event_name, Event, Event_type, Event_location

from telegram.telegram_base import send_telegram_message
from forms.parser import create_event
import wget
from django.forms.models import model_to_dict
from .forms import SpectForm










def index(request):       #-------------MAIN
    # if request.method == 'POST':
    #     if 'FindFile' in request.POST:
    #         wget.download(request.POST.get('FindFile'))


    if "command" in request.GET:    #-----ПАРСИНГ С САЙТА
        if 'go_parsing' in request.GET.get('command'):
            try:
                url = "https://mikhalkov12.ru/playbill/"
                this_month = datetime.datetime.now().month
                this_year = datetime.datetime.now().year
                url_list = [url]
                for i in range(2):
                    url_list.append(f"https://mikhalkov12.ru/playbill//?month={this_month+1+i}&year={this_year}")
                event_names = Event_name.objects.all()
                event_location = Event_location.objects.all()


                old_events = Event.objects.all()
                for url in url_list:
                    for name in create_event(url):
                        event_names = Event_name.objects.all()
                        event_location = Event_location.objects.all()
                        index = 0
                        for event in event_names:

                            if name['name'] == str(event):
                                index = 1
                        if index == 0:
                            record = Event_name(name=name['name'])
                            record.save()

                        for event_l in event_location:

                            if name['location'] == str(event_l.location):
                                index = 1
                        if index == 0:
                            record_l = Event_location(location=name['location'].strip())
                            record_l.save()
                    for new_event in create_event(url):
                        control_str = ''
                        str_from_request = f'{new_event["date"]}{new_event["name"]}Спектакль'
                        location = new_event['location'].strip()
                        control_index = 0
                        for i in old_events:
                            control_str = f'{i.date}{i.name}{i.type}'
                            str_from_request = f'{new_event["date"]}{new_event["name"]}Спектакль'
                            if control_str == str_from_request:
                                control_index = 1

                        if control_index == 0:
                            record = Event(date=new_event['date'], name=Event_name.objects.get(name=new_event['name']), type=Event_type.objects.get(type="Спектакль"))
                            record.save()
            except:
                print('Что-то пошло не так...')



        return redirect('/')
                #--------ПАРСИНГ С САЙТА







    try:
        author = f"{request.user.first_name} {request.user.last_name}"
    except:
        author = request.user.username
    if 'text_message' in request.GET:
        if request.user.is_staff:
            send_telegram_message(request.GET.get('text_message'), author=author)
            return(redirect('/'))
    if 'month' in request.GET:
        setattr(my_calendar, 'current_month', int(request.GET.get('month')))
    if 'year' in request.GET:

        if request.GET.get('year') == 'current':
            setattr(my_calendar, 'current_year', calendar_switch_year()['current_year'])
        if request.GET.get('year') == 'next':
            setattr(my_calendar, 'current_year', calendar_switch_year()['next_year'])
        if request.GET.get('year') == 'real':
            setattr(my_calendar, 'current_year', calendar_switch_year()['real_year'])
        setattr(my_calendar, 'year_title', my_calendar.current_year)
    if 'home' in request.GET:
        setattr(my_calendar, 'current_year', datetime.datetime.now().year)
        setattr(my_calendar, 'year_title', datetime.datetime.now().year)
        setattr(my_calendar, 'current_month', datetime.datetime.now().month)
    if request.user.is_authenticated:#-------TODAY
        today = f'#id_card_{datetime.datetime.now().day}'
        card_bg_color = 'background-color: #07bc25'
        if 'month' in request.GET:
            if int(request.GET.get('month')) == datetime.datetime.now().month:
                today = autoscroll()
                card_bg_color = 'background-color: #07bc25'
            else:
                today = '#main'
                card_bg_color = ''#------TODAY


        return render(request, 'main/index.html', context={'cal':calendar(result='', user_valid=request.user.is_staff,card_header_bg_color=card_bg_color, author=author), 'current_month': my_calendar.month_text[my_calendar.current_month], 'btn_month': calendar_switch_month(), 'current_year': calendar_switch_year()['current_year'], 'next_year': calendar_switch_year()['next_year'], 'real_year': calendar_switch_year()['real_year'], 'today': today, 'year_title': my_calendar.year_title})
    else:
        return redirect('login')



def about(request):#--------------------------------------------ABOUT
    return render(request, 'main/about.html')


def spects(request):
    if request.method == 'POST':
        if 'deleteSpect' in request.POST:
            spect = Spect.objects.get(id=request.POST.get('deleteSpect'))
            shutil.rmtree(f'materials/{spect.name}')
            spect.delete()
            spect = Spect.objects.all
            context = {
                'spects': spect
            }
            return redirect('spects')


    spect = Spect.objects.all
    context = {
        'spects': spect
    }

    return render(request, 'main/spects.html', context=context)


def add_spect(request):
    if request.method == 'POST':
        form = SpectForm(request.POST, request.FILES)
        if form.is_valid():
            spect = form.save(commit=False)

            spect.label = request.POST.get('name')
            print(spect.label)


            spect.save()
            try:
                os.rename('materials/q', f'materials/{spect.label}')
            except:
                pass
            try:
                os.mkdir(f'materials/{spect.label}')
            except:
                pass

            return redirect('spects')

    else:
        form = SpectForm()





    context = {
        'form': form
    }
    return render(request, 'main/add_spect.html', context=context)


def edit_spect(request):
    context = {

    }
    if request.method == 'GET':
        if 'id' in request.GET:
            spect = Spect.objects.get(id=request.GET.get('id'))
            video_url = str(spect.video).split('/')[-1]
            print (video_url)
            context = {
                'spect': spect,
                'video': video_url,
            }
    if request.method == 'POST':
        if 'btn-save-video' in request.POST:
            spect = Spect.objects.get(id=request.POST.get('btn-save-video'))
            spect.video = request.POST.get('newVideo')
            spect.save()
            video_url = str(spect.video).split('/')[-1]
            print (video_url)
            context = {
                'spect': spect,
                'video': video_url,
            }

    return render(request, 'main/edit_spect.html', context=context)



def load_file(request):
    if request.method == 'GET':
        if 'id' in request.GET:
            try:
                spect = Spect.objects.get(id=request.GET.get('id'))
                folder = spect.name
                file = str(request.GET.get('path')).split('/')[-1]
                format_file = str(request.GET.get('path')).split('.')[-1]
                if format_file == 'pdf':
                    content_type = 'application/pdf'
                elif format_file == 'png':
                    content_type = 'image/png'
                elif format_file == 'jpeg':
                    content_type = 'image/jpeg'
                elif format_file == 'JPG':
                    content_type = 'image/JPG'
                elif format_file == 'txt':
                    print('sfgdsgf')
                    with open(request.GET.get('path'), 'r') as f:
                        return HttpResponse(f)

                else:
                    return FileResponse(open(request.GET.get('path'), 'rb'),
                                    filename=file,
                                    as_attachment=True,
                                    )
                return FileResponse(open(request.GET.get('path'), 'rb'),
                                    filename=file,
                                    as_attachment=False,
                                    content_type=content_type,
                                    )
            except:
                pass


def handle_uploaded_file(f, name,  folder):
    with open(f'materials/{name}/{folder}/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def folder(request):
    if request.method == 'GET':
        if 'folder' in request.GET and 'id' in request.GET:
            spect = Spect.objects.get(id=request.GET.get("id"))
            path = f'materials/{spect.name}/{request.GET.get("folder")}'
            try:
                os.mkdir(path)
                list_file = os.listdir(path)
                print(list_file)
            except:

                list_file = os.listdir(path)
                print(list_file)
            context = {
                'spect': spect,
                'folder': request.GET.get("folder"),
                'files': list_file,
            }
            if 'status' in request.GET:
                if request.GET.get('status') == 'delete':
                    try:
                        os.remove(request.GET.get('path'))
                    except:
                        pass
            return render(request, 'main/folder.html', context=context)

    if request.method == 'POST':
        if 'addFile' in request.POST:
            print(request.FILES.getlist('upload_files', [])[0])
            spect = Spect.objects.get(id=str(request.POST.get("addFile")).split('$')[0])
            folder = str(request.POST.get("addFile")).split('$')[1]
            for file in request.FILES.getlist('upload_files', []):

                handle_uploaded_file(file, spect.name, folder)
            path = f'materials/{spect.name}/{folder}'
            list_file = os.listdir(path)
            context = {
                'spect': spect,
                'folder': folder,
                'files': list_file,
            }
            return render(request, 'main/folder.html', context=context)
