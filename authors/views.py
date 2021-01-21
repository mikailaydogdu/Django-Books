from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from home.models import Author, Quotations
import random
# Create your views here.


def author(request):
    author = Author.objects.all()
    context = {
        "author": author,

    }
    return render(request, 'authors.html', context)

def author_details(request, slug):
    article = get_object_or_404(Author, slug=slug)
    alıntılar = Quotations.objects.filter(artist_id=article.id)

    context = {
        "article": article,
        "alıntılar": alıntılar,
    }
    return render(request, 'details.html', context)


