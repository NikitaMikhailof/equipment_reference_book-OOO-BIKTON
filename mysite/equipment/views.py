from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Category, Equipment
from taggit.models import Tag
from django.core.paginator import Paginator
from django.views.generic import ListView



class PostListView(ListView):
    queryset = Equipment.objects.all()
    count = queryset.count()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'equipment/index.html'

    extra_context = {
        'title': 'Главная страница',
        'count': count
    }



def show_post(request, post_slug):
    post = get_object_or_404(Equipment, slug=post_slug)
    data = {'title': post.title,
            'cats': Category.objects.all(),
            'post': post}
    return render(request, 'equipment/post.html', context=data)



def show_posts_category(request, cat_slug):
    c = get_object_or_404(Category, slug=cat_slug)
    posts_list = Equipment.objects.filter(cat__slug=cat_slug) 
    count = posts_list.count()
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    data = {'title': c.title,
            'count': count,
            'cats': Category.objects.all(),
            'posts': posts} 
    return render(request, 'equipment/show_posts_category.html', context=data)



def show_posts_tags(request, tag_slug):
    t = get_object_or_404(Tag, slug=tag_slug)
    posts_list = Equipment.objects.filter(tags__slug=tag_slug)
    count = posts_list.count()
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    data = {'title': t.name,
            'count': count,
            'cats': Category.objects.all(),
            'posts': posts} 
    return render(request, 'equipment/show_posts_category.html', context=data)



