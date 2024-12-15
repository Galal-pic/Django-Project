from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# # Create your views here.
# def home(request):
#     return render(request,'home.html')
# def about(request):
#     return render(request,'about.html')

def post_list(request):
    Posts = Post.objects.all()
    return render(request,'blog/post/list.html',{'posts':Posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,
                              slug = post,
                              publish__year = year,
                              publish__month = month,
                              publish__day = day)
    return render(request,'blog/post/detail.html',{'post':post})

