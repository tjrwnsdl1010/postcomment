from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', id=post.id)

    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/form.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    comment_form = CommentForm()

    comments = post.comment_set.all()

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, 'posts/detail.html', context)


def comments_create(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 1.
            comment.post_id = post_id
            # 2. 
            # post = Post.objects.get(id=post_id)
            # comment.post = post
            
            comment.save()

            return redirect('posts:detail', post_id)

    else:
        return redirect('posts:detail', post_id)


def comments_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)

    comment.delete()

    return redirect('posts:detail', post_id)