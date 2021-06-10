from django import template

register = template.Library()

@register.filter(name='get_class')
def get_class(item):
    return str(item.__class__).replace("'",'').replace('>','').split('.')[-1]