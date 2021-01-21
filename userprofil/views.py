from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from .forms import profileForm

# Create your views here.


def user_profile(request):
    form = profileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        return redirect('user_profile')
    else:
        update = profileForm(instance=request.user)
    
    return render(request, 'user_profile.html')

def comment_list(request):
    comments = Comment.objects.filter(author_id=request.user.id)

    context = {
        'comments':comments,
    }
    return render(request, 'comment_list.html', context)


def delete(request, id):
    comments = get_object_or_404(Comment, id=id)
    comments.delete()
    return redirect('comment_list')

