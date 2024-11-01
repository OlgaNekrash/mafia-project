from django.shortcuts import render
from blog.models import BlogPost


def home(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'home_page/home.html', {'blog_posts': blog_posts})
