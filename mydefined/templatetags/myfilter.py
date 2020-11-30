from django import template

register = template.Library()


# noinspection SpellCheckingInspection
@register.filter(name='replace')
def do_replace(value, agrs):
    old_value = agrs.split(':')[0]
    new_value = agrs.split(':')[1]
    return value.replace(old_value, new_value)
