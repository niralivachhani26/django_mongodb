from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from bson import ObjectId
from django.http import HttpResponse

# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Create a new product
def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = float(request.POST.get("price"))
        stock = int(request.POST.get("stock"))

        # Creating and saving a new Product document
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock
        )
        product.save()
        return redirect("product_list")  # Redirect to a product list page

    return render(request, 'product_form.html')

# Update an existing product
def product_update(request, pk):
    if not ObjectId.is_valid(pk):
        return HttpResponse("Invalid Product ID", status=400)
    product = Product.objects.get(id=pk)
    context ={
        'product':product
    }
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            description = request.POST.get("description")
            price = request.POST.get("price",0)
            stock = request.POST.get("stock",0)
            product = Product.objects.get(id=pk)
            product.name = name
            product.price = float(price)
            product.stock = int(stock)
            product.description = description
            product.save()
            return redirect("product_list")
        except Product.DoesNotExist:
            return HttpResponse("Product not found.", status=404)
    return render(request, 'product_form.html',context)

# Delete a product
def product_delete(request, pk):
    if not ObjectId.is_valid(pk):
        return HttpResponse("Invalid Product ID", status=400)

    deleted_count = Product.objects(id=pk).delete()
    if deleted_count:
        return redirect('product_list')
    else:
        return render(request, 'product_confirm_delete.html', {'product': product})

