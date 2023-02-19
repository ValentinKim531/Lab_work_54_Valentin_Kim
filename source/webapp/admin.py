from django.contrib import admin

from webapp.models import Categories, Goods

# Register your models here.

class Categories_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    fields = ('name', 'description')

admin.site.register(Categories, Categories_Admin)
class Goods_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'price', 'image')
    list_filter = ('id', 'name', 'description', 'category', 'price', 'image')
    search_fields = ('name', 'description', 'category', 'price')
    fields = ('name', 'description', 'category', 'price', 'image')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Goods, Goods_Admin)