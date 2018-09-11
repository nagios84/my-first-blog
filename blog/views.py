from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_url', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post = form.save()
            return redirect('post_detail_url', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})