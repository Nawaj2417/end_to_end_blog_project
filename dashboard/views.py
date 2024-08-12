from django.http import HttpResponse
from django.shortcuts import render
from HOME.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    total_views = Blog.objects.aggregate(total_views=Sum('views'))['total_views']
    total_comments = Comment.objects.count()
    total_posts = Blog.objects.count()
    post = Blog.objects.order_by('-id')

    context = {
        'total_views': total_views,
        'total_comments': total_comments,
        "total_posts" : total_posts,
        'post' : post 
    }


    return render(request, "dashboard/dash.html", context)
@login_required

def blog(request):
    post = Blog.objects.order_by('-id')

    context = {
        'post':post
    }
    return render(request, "dashboard/dash_blog.html",context)
@login_required

def comment(request):
    all_comments = Comment.objects.select_related('post').order_by('-date')
    context = {
        'all_comments': all_comments
    }

    return render(request,"dashboard/comments.html",context)

@login_required

def page(request):
    return render(request, "dashboard/page.html")