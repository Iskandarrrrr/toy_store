from django import template
from shop.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-views': 'Views ⬆',
        'views': 'Views ⬇',
        '-title': 'A - Z',
        'title': 'Z - A',
        '-created_at': 'New',
        'created_at': 'Old'
    }
    return sorters
