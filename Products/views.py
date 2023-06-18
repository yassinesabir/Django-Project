from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import GestionProduits


# Create your views here.

def index(request):
    Products = Product.objects.all()
    return render(request,'Products/index.html',{'products':Products})
    
def detail(request, Product_id):
    # product = Product.objects.get(id=Product_id)
    product = get_object_or_404(Product, id=Product_id)
    return render(request,'Products/detail.html',{'Product':product})

def editProducts(request):
    form=GestionProduits(request.POST or None)
    print(request.POST.get("name"))
    nom="SABIR Yassine"
    if form.is_valid():
        form = GestionProduits()
    contexte={
        "nom":nom,
        "form":form,
    }
    return render(request, "Products/editProducts.html", contexte)

