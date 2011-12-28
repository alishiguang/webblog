# Create your views here.


from webblog.blog.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/index/")
    else:
        form = UserCreationForm()
    return render_to_response('register.html', {'form':form})

def index(request):

    before_range_num = 1
    after_range_num = 1

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    article_list = Article.objects.all()
    paginator = Paginator(article_list, 2)


    try:
        articlelist = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        articlelist = paginator.page(1)
        if page >= after_range_num:
            page_range = paginator.page_range[page-after_range_num:page+before_range_num]
        else:
            page_range = paginator.page_range[0:int(page)+before_range_num]

    return render_to_response('index.html',locals())