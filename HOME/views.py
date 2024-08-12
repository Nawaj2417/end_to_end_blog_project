from django.http import HttpResponse
from django.shortcuts import render
from .models import*
from django.shortcuts import render , get_object_or_404, redirect


# Create your views here.
def index(request):
    post = Blog.objects.order_by('-id')
    main_post = Blog.objects.order_by('-id').filter(Main_post = True)[0:1]
    recent = Blog.objects.filter(section = 'Recent').order_by('-id')[:5]
    popular = Blog.objects.filter(section='Popular').order_by('-id')[0:5]
    cat = Category.objects.all()

    context = {
        'post': post,
        'main_post': main_post,
        'recent': recent, 
        'cat' : cat,
        'popular': popular

    }
    
    return render(request, "index.html", context)


def blog_detail(request,slug):
    # posts= Blog.objects.order_by('-id')
    category = Category.objects.all()
    post = get_object_or_404(Blog, blog_slug = slug)
#   increment view count
    post.views +=1
    post.save()

    comments = Comment.objects.filter(blog_id = post.id).order_by('-date')

    context = {
        # 'posts': post,
         'category': category,
         'post' : post,
         'comments': comments
 
    }

    return render (request, "blog_detail.html", context)


def category(request, slug):
    cat = category.objects.all()
    blog_cat = category.objects.filter(slug=slug)
    context = {
        'cat': cat,
        'active_category' : slug,
        "blog_cat" : blog_cat,

    }
    return render (request, 'category.html',context)

def add_comment(request,slug):
     
    if request.method == 'POST':
        post = get_object_or_404(Blog, blog_slug = slug)
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        website = request.POST.get('InputWeb')
        comment_text = request.POST.get('InputComment')
        parent_id = request.POST.get('parent_id')
        parent_comment = None
        
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)

        Comment.objects.create(
            post= post,
            name=name,
            email=email,
            website=website,
            comment=comment_text,
            parent=parent_comment
        )
        return redirect("blog_detail",slug=post.blog_slug)
    return redirect('blog_detail')


