from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseNotFound
from .forms import *


def home(request):
    posts = Article.objects.all()
    context = {'posts': posts}
    return render(request, 'news/home.html', context=context)


def football(request):
    posts = Article.objects.filter(category=7)
    context = {'posts': posts}
    return render(request, 'news/football.html', context=context)


def basketball(request):
    posts = Article.objects.filter(category=8)
    context = {'posts': posts}
    return render(request, 'news/basketball.html', context=context)


def hockey(request):
    posts = Article.objects.filter(category=9)
    context = {'posts': posts}
    return render(request, 'news/hockey.html', context=context)


def mma(request):
    posts = Article.objects.filter(category=10)
    context = {'posts': posts}
    return render(request, 'news/ufc.html', context=context)


def tennis(request):
    posts = Article.objects.filter(category=11)
    context = {'posts': posts}
    return render(request, 'news/tennis.html', context=context)


def biathlon(request):
    posts = Article.objects.filter(category=12)
    context = {'posts': posts}
    return render(request, 'news/biathlon.html', context=context)


def add_post(request):
    posts = Article.objects.all()
    form = AddArticle()
    context = {'posts': posts, 'form': form}
    if request.method == 'POST':
        form = AddArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'news/add_post.html', context=context)


def epl(request):
    posts = Article.objects.filter(football_category=1)
    context = {'posts': posts}
    return render(request, 'news/epl.html', context=context)


def laliga(request):
    posts = Article.objects.filter(football_category=2)
    context = {'posts': posts}
    return render(request, 'news/laliga.html', context=context)


def seria_a(request):
    posts = Article.objects.filter(football_category=3)
    context = {'posts': posts}
    return render(request, 'news/seriaa.html', context=context)


def bundesliga(request):
    posts = Article.objects.filter(football_category=4)
    context = {'posts': posts}
    return render(request, 'news/bundesliga.html', context=context)


def ligue1(request):
    posts = Article.objects.filter(football_category=5)
    context = {'posts': posts}
    return render(request, 'news/ligue1.html', context=context)


def ucl(request):
    posts = Article.objects.filter(football_category=6)
    context = {'posts': posts}
    return render(request, 'news/cl.html', context=context)


def nhl(request):
    posts = Article.objects.filter(hockey_category=1)
    context = {'posts': posts}
    return render(request, 'news/nhl.html', context=context)


def hockey_by(request):
    posts = Article.objects.filter(hockey_category=2)
    context = {'posts': posts}
    return render(request, 'news/hockeyby.html', context=context)


def nba(request):
    posts = Article.objects.filter(basketball_category=1)
    context = {'posts': posts}
    return render(request, 'news/nba.html', context=context)


def euroleague(request):
    posts = Article.objects.filter(basketball_category=2)
    context = {'posts': posts}
    return render(request, 'news/euroleague.html', context=context)


def handler404(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
