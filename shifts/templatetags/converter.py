from django import template

register = template.Library()

@register.filter(name='titleConverter')
def titleConverter(param):
    if param == '0profdr':
        return 'Prof. Dr.'
    elif param == '1docdr':
        return 'Doç. Dr.'
    elif param == '2dr':
        return 'Dr.'
    elif param == '3arastirmadr':
        return 'Araştırma Görevlisi Dr.'
    elif param == '4arastirma':
        return 'Araştırma Görevlisi'
    else:
        return None