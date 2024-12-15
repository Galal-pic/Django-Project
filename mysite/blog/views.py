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

def post_detail(request,id):
    posts = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    print(posts)
    return render(request,'blog/post/detail.html',{'post':posts})

