from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    productos = Producto.objects.filter(disponible=True)[:6]
    return render(request, 'home.html', {'productos': productos})