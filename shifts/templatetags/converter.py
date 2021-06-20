from django import template

register = template.Library()

@register.filter(name='titleConverter')
def titleConverter(param):
    if param == 'Null':
        return ''
    else:
        return param