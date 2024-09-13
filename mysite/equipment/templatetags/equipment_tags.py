from django import template
import equipment.views as views
from equipment.models import Category, Equipment, Comment
from taggit.models import Tag



register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all() 



@register.simple_tag()
def get_tags():
    return Tag.objects.all()


@register.simple_tag()
def get_most_commented_posts():
    comments = Comment.objects.order_by('-time_create')[:5]
    return comments.select_related('post') 