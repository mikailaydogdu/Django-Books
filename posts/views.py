from django.shortcuts import render, HttpResponseRedirect
from .models import Posts, Comment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.contrib import messages


# Create your views here.

def posts(request):
    posts = Posts.objects.all()
    context = {
        "posts": posts,

    }
    return render(request, 'posts.html', context)

def posts_details(request, slug):
    posts_details = get_object_or_404(Posts, slug=slug)
    comment_content = Comment.objects.filter(article_id=posts_details.id)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = posts_details
        comments = form.save(commit=False)
        comments.author = request.user
        form.save()
        return HttpResponseRedirect(posts_details.slug)

    
    context = {
        "posts_details": posts_details,
        'comment_content': comment_content,
        'form': form,
    }
    return render(request, 'post_details.html', context)
