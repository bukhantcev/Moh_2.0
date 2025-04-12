import datetime
from calendar import monthrange
from forms.models import Event, Event_type
from department_events.models import DepartmentEvent, DepartmentEventType
from django.template.loader import render_to_string

#----------------------------------------CALENDAR
month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
current_year = datetime.datetime.now().year
current_month = month_text[datetime.datetime.now().month]


class Calendar:
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    year_title = current_year

    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    def cal_text(current_month):
        return month_text(current_month)

my_calendar = Calendar


def calendar(result='', user_valid=False, card_header_bg_color='', user=None):
    current_year = my_calendar.current_year
    current_month = my_calendar.current_month
    days_quantity = monthrange(current_year, current_month)[1]
    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}

    for i in range(days_quantity):
        today_color = card_header_bg_color if i+1 == datetime.datetime.now().day else ''
        event_li = ''
        department_li = ''
        date = datetime.datetime(current_year, current_month, i+1)
        event_object = Event.objects.order_by('date')
        if hasattr(user, 'profile') and (user.profile.is_bigboss or user.is_superuser):
            department_object = DepartmentEvent.objects.order_by('datetime')
        else:
            department_object = DepartmentEvent.objects.filter(department=user.profile.podrazdelenie).order_by('datetime')
        event_type_for_color = Event_type.objects
        for dep_event in department_object:
            if str(date.date()) == str(dep_event.datetime.date()):
                id = f'department_event_id{dep_event.id}'
                ev_name = dep_event.name
                ev_date = dep_event.datetime
                ev_time = f'{str(ev_date).split(" ")[1].split(":")[0]}:{str(ev_date).split(" ")[1].split(":")[1]}'
                ev_type = dep_event.type
                btn_color = f'background-color: green; border-color: red'
                ev_location = dep_event.location
                ev_utochneniya = f'<h5 style="color: red">Описание:<br></h5><p>{dep_event.description}</p>' if dep_event.description and dep_event.description.strip() else ''
                ev_staff = '<br>'.join([
                    f'<a href="tel:{p.phone}">{p.last_name} {p.first_name[0]}.</a>'
                    for p in dep_event.staff.all()
                    if p.last_name and p.first_name and p.phone
                ])

                department_li += render_to_string('main/event_item.html', {
                    'user_valid': hasattr(user, 'profile') and user.profile.is_boss,
                    'event': dep_event,
                    'date': date.strftime('%Y-%m-%d'),
                    'ev_time': ev_time,
                    'btn_color': btn_color,
                    'menu_html': render_to_string('department_events/dep_menu.html', {'event': dep_event}) if hasattr(user, 'profile') and user.profile.is_boss else '',
                    'ev_utochneniya': ev_utochneniya,
                    'ev_staff': ev_staff,
                    'action_buttons': render_to_string('department_events/dep_actions.html', {'event': dep_event}) if hasattr(user, 'profile') and user.profile.is_boss else '',
                    # 'button_tg_html': f'<a href="?text_message={dep_event.id}" class="btn btn-info btn-sm">Отправить в телегу</a>',
                    'button_tg_html': '',
                    'is_bigboss': hasattr(user, 'profile') and user.profile.is_bigboss,
                    'is_boss': hasattr(user, 'profile') and user.profile.is_boss,
                    'is_super': user.is_superuser,
                    'depart': True,
                })

        for event in event_object:
            button_tg_html = f'<a href="?text_message={event.id}" class="btn btn-info btn-sm">Отправить в телегу</a>' if user_valid else ''
            if str(date.date()) == str(event.date.date()):
                id = f'event_id{event.id}'
                ev_name = event.name
                ev_date = event.date
                ev_time = f'{str(ev_date).split(" ")[1].split(":")[0]}:{str(ev_date).split(" ")[1].split(":")[1]}'
                ev_type = event.type
                event_type_for_color = Event_type.objects.get(type=str(ev_type))
                btn_color = f'background-color: {event_type_for_color.button_color}; border-color: {event_type_for_color.button_color}'
                ev_location = event.location
                ev_utochneniya = f'<h5 style="color: red">Описание:<br></h5><p>{event.utochneniya}</p>' if event.utochneniya and event.utochneniya.strip() else ''
                staff_lines = []
                if event.svet == 'Да':
                    staff_lines.append('Свет')
                if event.zvuk == 'Да':
                    staff_lines.append('Звук')
                if event.video == 'Да':
                    staff_lines.append('Видео')
                if event.decor == 'Да':
                    staff_lines.append('Декорации')
                if event.rekvizit == 'Да':
                    staff_lines.append('Реквизит')
                if event.grim == 'Да':
                    staff_lines.append('Грим')
                if event.kostum == 'Да':
                    staff_lines.append('Костюм')
                ev_staff = '<br>'.join(staff_lines)

                event_li += render_to_string('main/event_item.html', {
                    'user_valid': user_valid,
                    'event': event,
                    'date': date.strftime('%Y-%m-%d'),
                    'ev_time': ev_time,
                    'btn_color': btn_color,
                    'menu_html': render_to_string('main/event_menu.html', {'event': event}) if user_valid else '',
                    'ev_utochneniya': ev_utochneniya,
                    'ev_staff': ev_staff,
                    'action_buttons': render_to_string('main/event_actions.html', {'event': event}) if user_valid else '',
                    'button_tg_html': button_tg_html,
                    'is_bigboss': hasattr(user, 'profile') and user.profile.is_bigboss,
                    'depart': False,
                    'is_super': user.is_superuser,
                })

        day_html = render_to_string('main/calendar_day.html', {
            'day_index': i + 1,
            'weekday': weekdays[date.weekday()],
            'today_color': today_color,
            'plus_button': render_to_string('main/plus_button.html', {'date': date.date()}) if user_valid else '',
            'event_li': event_li,
            'department_li': department_li,
            'date': date.strftime('%Y-%m-%d'),
            'full_date': date.strftime('%Y-%m-%d'),
            'profile': user.profile,
            'show_menu': user_valid or (hasattr(user, 'profile') and (user.profile.is_boss or user.is_superuser)),
            'user': user,
        })
        result += day_html
    return render_to_string('main/calendar_view.html', {'days_html': result})

def calendar_switch_month(): #---------------------MONTS
    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    result = []
    final = ''
    ind2 = 0
    for i in range(11):
        ind = my_calendar.current_month
        if i < (12-ind):
            ind = ind+i +1
            result.append(ind)
        else:
            ind2 = ind2 + 1
            result.append(ind2)
    for i in result:
        final = final + f'<li><a class="dropdown-item" href="?month={i}" type="submit">{month_text[i]}</a></li>' + '\n'

    return final


def calendar_switch_year(): #__________________________________YEARS
    current_year = my_calendar.current_year
    next_year = my_calendar.current_year + 1
    real_year = datetime.datetime.now().year
    return {'current_year': current_year, 'next_year': next_year, 'real_year': real_year}
#----------------------------------------------------------------------------------------CALENDAR


#--------------Autoscroll today______------------

def autoscroll():
    today =f'#id_card_{datetime.datetime.now().day}'

    return today
