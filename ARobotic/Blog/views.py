from django.shortcuts import render
from .models import Article, Image, Tag,Category, Comment
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from django.core.paginator import Paginator
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.
def search(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(headline__icontains=query)
    paginator = Paginator(articles, 1)
    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    # Get the current page object from the paginator
    page_obj = paginator.get_page(page_number)
    context = {
        'query': query,
        'articles': articles,
        'page_obj': page_obj
    }
    return render(request, 'Blog/get/search.html', context)

def index(request):
    articles=Article.objects.order_by('-pub_date')
    articles_slider = articles[:5]
    articles_robots = articles.filter(categories__name='Robots')[:5]
    articles_programming = articles.filter(categories__name='Programming')[:5]
    articles_electronics = articles.filter(categories__name='Electronics')[:5]
    articles_printing = articles.filter(categories__name='Printing')[:5]
    articles_arduino = articles.filter(categories__name='Arduino')[:3]
    articles_rasberry = articles.filter(categories__name='RasberryPi')[:3]
    img = Image.objects.all()
    context = {
        'articles':articles, 
        'img':img,
        'articles_slider':articles_slider,
        'articles_robots':articles_robots,
        'articles_programming':articles_programming,
        'articles_electronics':articles_electronics,
        'articles_printing':articles_printing,
        'articles_arduino':articles_arduino,
        'articles_rasberry':articles_rasberry,

    }
    return render(request, "Blog/index.html", context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "blog/article.html", context)

def articles_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    articles = Article.objects.filter(tags=tag)
    # Create a paginator object with 10 articles per page
    paginator = Paginator(articles, 10)
    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    # Get the current page object from the paginator
    page_obj = paginator.get_page(page_number)
    context = {
        'tag': tag,
        'articles': articles,
        'page_obj': page_obj
    }
    return render(request, "blog/get/by_tag.html", context)

def articles_by_category(request, category):
    category_id = Category.objects.get(name=category)
    articles = Article.objects.filter(categories=category_id)
    # Create a paginator object with 10 articles per page
    paginator = Paginator(articles, 10)
    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    # Get the current page object from the paginator
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'page_obj': page_obj,
        'category': category,
    }
    return render(request, "blog/get/category.html", context)




