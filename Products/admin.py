from django.contrib import admin
from .models import *
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display=('id','nom')
    search_fields=('id','nom')

class ProductImageAdmin(admin.StackedInline):
    model =ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','qte_stock','price','size','date_creation','categorie','subcategorie')
    search_fields=('name','nom_categorie')
    inlines = [ProductImageAdmin]

class ProfilAdmin(admin.ModelAdmin):
    list_display=('username','Cin_Number','address','phone_Number','email')

admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Subcategorie,CategorieAdmin)
admin.site.register(Size,CategorieAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Profil,ProfilAdmin)
admin.site.register(ProductImage)