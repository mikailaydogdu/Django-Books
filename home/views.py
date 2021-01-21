from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from .models import Author, Quotations, Quotation
import random

# Create your views here.

def explore(request):
    qindex = list(Quotation.objects.all())
    random.shuffle( qindex )
    result = qindex[:100]

    context = {
        'page_obj': result,
        }
    return render(request, 'home/keşfet.html', context)

