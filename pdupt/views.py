from django.shortcuts import render

from authors.models import Authors
from papers.models import Papers

def index(request):
    context = {
        'title': 'Halaman Utama',
    }
    return render(request, 'index.html', context)

def find(request):
    return render(request, 'find.html')

def search(request):
    if request.method == 'POST':
        catch = request.POST['query']
        print(catch)
        papers = Papers.objects.filter(title__icontains=catch)[:5]
        authors = Authors.objects.filter(name__icontains=catch)[:5]
        print(papers, authors)
        context = {
            'title': 'Halaman Utama',
            'Papers': papers,
            'Authors': authors,
            'catch': catch
        }
        return render(request, 'search.html', context)
