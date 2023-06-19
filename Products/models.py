from django.db import models
from django.utils import timezone
# from django.utils.safestring import mark_safe
# from django.utils.text import slugify

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.category_name)
    #     super(Categorie ,self).save(*args , **kwargs)

    def __str__(self) :
        return self.nom

class Subcategorie(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self) :
        return self.nom
    
class Size(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self) :
        return self.nom
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    qte_stock = models.IntegerField()
    price = models.FloatField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    subcategorie = models.ForeignKey(Subcategorie, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)

    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super(Product ,self).save(*args , **kwargs)

    def __str__(self) :
        return self.name + ' ' + self.subcategorie.nom

class Profil(models.Model):
    username = models.CharField(max_length=255)
    Cin_Number = models.CharField(max_length=10)
    address = models.CharField(max_length=355)
    phone_Number = models.IntegerField()
    email = models.CharField(max_length=355)


class ProductImage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="product")














# image= models.ImageField(upload_to = '../../static/images')
# def admin_photo(self):
#     return mark_safe('<img src ="{}" width="100" />' .format(self.image.url))
# admin_photo.short_description = 'Image'
# admin_photo.allow_tags = True