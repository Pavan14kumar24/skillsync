from django import template

register = template.Library()

@register.filter
def dict_key(d, key):
    """Allows dictionary lookup in Django templates: {{ mydict|dict_key:some_key }}"""
    return d.get(key, 0)