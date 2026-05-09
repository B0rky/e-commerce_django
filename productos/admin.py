from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'disponible', 'categoria')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre', 'sku')
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ('precio', 'stock', 'disponible')