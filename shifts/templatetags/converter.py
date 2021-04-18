from django import template

register = template.Library()

@register.filter(name='titleConverter')
def titleConverter(param):
    if param == 'profdr':
        return 'Prof. Dr.'
    elif param == 'docdr':
        return 'Doç. Dr.'
    elif param == 'dr':
        return 'Dr.'
    elif param == 'arastirmadr':
        return 'Araştırma Görevlisi Dr.'
    elif param == 'arastirma':
        return 'Araştırma Görevlisi'
    else:
        return None