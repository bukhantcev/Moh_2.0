from django import template

register = template.Library()

@register.filter(name='chet')
def chet(value):
    if int(value) % 2 == 0:
        return True
    else:
        return False


