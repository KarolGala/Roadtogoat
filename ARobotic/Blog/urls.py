from django.urls import path,include
from . import views



urlpatterns = [
    path('',  views.index, name="index"),
    path('search', views.search, name='search'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('tag/<str:tag_name>/', views.articles_by_tag, name='articles_by_tag'),
    path('category/<str:category>/', views.articles_by_category, name='articles_by_category'),
]

