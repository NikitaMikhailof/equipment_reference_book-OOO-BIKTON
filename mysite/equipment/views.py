from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Category, Equipment
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from . forms import SearchForm
from django.contrib.postgres.search import TrigramSimilarity

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='/account/login')
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Equipment.objects.annotate(similarity=TrigramSimilarity('title', query)) \
                                       .filter(similarity__gte=0.1).order_by('-similarity')
    return render(request,
                 'equipment/search.html',
                 {'form': form,
                 'query': query,
                 'results': results
                 })


class PostListView(LoginRequiredMixin,ListView):
    login_url = '/account/login'
    queryset = Equipment.objects.all()
    count = Equipment.objects.count()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'equipment/index.html'

    extra_context = {
        'title': 'Главная страница',
        'count': count
    }


@login_required(login_url='/account/login')
def show_post(request, post_slug):
    post = get_object_or_404(Equipment, slug=post_slug)
    data = {'title': post.title,
            'cats': Category.objects.all(),
            'post': post}
    return render(request, 'equipment/post.html', context=data)


@login_required(login_url='/account/login')
def show_posts_category(request, cat_slug):
    c = get_object_or_404(Category, slug=cat_slug)
    posts_list = Equipment.objects.filter(cat__slug=cat_slug) 
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data = {'title': c.title,
            'total': posts_list.count(),
            'cats': Category.objects.all(),
            'posts': posts} 
    return render(request, 'equipment/show_posts_category.html', context=data)


@login_required(login_url='/account/login')
def show_posts_tags(request, tag_slug):
    t = get_object_or_404(Tag, slug=tag_slug)
    posts_list = Equipment.objects.filter(tags__slug=tag_slug)
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)   
    data = {'title': t.name,
            'total': posts_list.count(),
            'cats': Category.objects.all(),
            'posts': posts} 
    return render(request, 'equipment/show_posts_category.html', context=data)



