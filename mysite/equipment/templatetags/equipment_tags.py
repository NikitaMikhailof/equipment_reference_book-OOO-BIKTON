from django import template
import equipment.views as views
from equipment.models import Category, Equipment
from taggit.models import Tag



register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all() 



@register.simple_tag()
def get_tags():
    return Tag.objects.all()