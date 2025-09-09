from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return dictionary[key] or 1 if key doesn't exist"""
    if dictionary and key in dictionary:
        return dictionary[key]
    return 1
