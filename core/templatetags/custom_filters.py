from django import template

register = template.Library()

@register.filter
def dict_key(d, key):
    """Safe dictionary lookup for templates."""
    if isinstance(d, dict):
        return d.get(key, 0)
    return 0