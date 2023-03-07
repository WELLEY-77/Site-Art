from django.shortcuts import render
from .models import GalleryArt

def home(request):
    galerias = GalleryArt.objects.all()
    return render(request, 'home/home.html', {'galerias':galerias})
