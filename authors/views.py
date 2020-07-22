from django.shortcuts import render

# Create your views here.

from .models import Authors

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    authors = Authors.objects.all()[:20]
    context = {
        'title': 'Halaman Utama',
        'Authors': authors
    }
    return render(request, 'authors/index.html', context)

def cobak(request):
    user_list = Authors.objects.all().order_by('nidn')[:100]
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 20)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'authors/author.html', { 'users': users })