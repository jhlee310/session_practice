from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Article, Category

# Create your views here.

def index(request):
    m_articles = Article.objects.filter(category = 1)
    d_articles = Article.objects.filter(category = 2)
    e_articles = Article.objects.filter(category = 3)
    m_category = Category.objects.get(id = 1)
    d_category = Category.objects.get(id = 2)
    e_category = Category.objects.get(id = 3)
    context = {
        'm_articles' : len(m_articles),
        'd_articles' : len(d_articles),
        'e_articles' : len(e_articles),
        'm_category' : m_category,
        'd_category' : d_category,
        'e_category' : e_category,
    }
    return render(request, 'blog/index.html', context)
    # return HttpResponse("메인 페이지입니다.")

def movie(request):
    m_articles = Article.objects.filter(category = 1)
    context = {
        'm_articles' : m_articles,
    }
    # return HttpResponse("영화 페이지에요.")
    return render(request, 'blog/movie.html', context)

def drama(request):
    d_articles = Article.objects.filter(category = 2)
    context = {
        'd_articles' : d_articles,
    }
    # return HttpResponse("드라마 페이지에요.")
    return render(request, 'blog/drama.html', context)

def entertain(request):
    e_articles = Article.objects.filter(category = 3)
    context = {
        'e_articles' : e_articles,
    }
    # return HttpResponse("예능 페이지에요.")
    return render(request, 'blog/entertain.html', context)


def detail(request, article_id):
    """
    기사 상세 내용 조회 페이지
    """
    an_article_for_detail = get_object_or_404(Article, pk=article_id)
    context = {'article' : an_article_for_detail}
    return render(request, 'blog/detail.html', context)

def new(request):
    """
    글 쓰기 페이지
    """
    if request.method == 'POST':
        c = 'category'
        d = Category(pk=c)
        e = d.name

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            create_date = timezone.now(),
            category = request.POST[e],
        )
        
        
            
        return redirect('blog/detail', article_id=new_article.pk)
    else:
        return render(request, 'blog/new.html')