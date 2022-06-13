from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import CommentForm


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


def delete_post(request, id):
    posts = Post.objects.all()
    context = {}

    obj = get_object_or_404(posts, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, 'delete_post.html', context)
