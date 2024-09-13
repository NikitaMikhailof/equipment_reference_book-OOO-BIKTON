from django.shortcuts import render, get_object_or_404
from . models import Category, Equipment, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from . forms import SearchForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.db.models import Q



@login_required(login_url='/account/login')
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Equipment.objects.filter(Q(title__icontains=query) | Q(title__iregex=query))

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
@require_POST
def post_comment(request, post_slug):
    post = get_object_or_404(Equipment, slug=post_slug)
    comment = None
    form = CommentForm(request, data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'equipment/comment.html',
                {'form': form,
                'post': post,
                'comment': comment})



@login_required(login_url='/account/login')
def show_post(request, post_slug):
    post = get_object_or_404(Equipment, slug=post_slug)
    comments = post.comments.all()
    form = CommentForm(request)
    form = CommentForm(request)
    data = {'title': post.title,
            'cats': Category.objects.all(),
            'comments': comments,
            'post': post,
            'form': form}
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



