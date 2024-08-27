from django.urls import path
from . import views 


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('show_posts/<slug:cat_slug>/', views.show_posts_category, name='show_posts_category'),
    path('show_tags/<slug:tag_slug>/', views.show_posts_tags, name='show_posts_tags'),
]
