from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context )

@login_required
def product(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)

@login_required
def product_detail(request, id):
    product = models.Product.objects.get(id=id)
    products = models.Product.objects.all()
    context = {
        'product': product,
        'products': products
    }    
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        models.Cart.objects.create(
            user=request.user,
            product_id=product_id,
            price=product.price,
            image=product.image,
        )
    return render(request, 'product-detail.html', context)

@login_required
def shoping_сart(request):
    total_price = 0
    carts = models.Cart.objects.filter(user=request.user)
    for cart in carts:
        total_price += cart.price 
    context = {
        'carts': carts,
        'total_price': total_price
    }
    return render(request, 'shoping_cart.html', context)

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def delete_cart(request, id):
    delete_product = models.Cart.objects.get(id=id)
    delete_product.delete()
    return redirect('shoping_cart')