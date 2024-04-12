from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Brand
from .forms import ProductForm
from checkout.forms import OrderStatusForm
from checkout.models import Order, OrderStatus


# Create your views here.
def all_products(request):
    """
    Render all products on the products page
    """
    products = Product.objects.all().order_by("-created_on")
    query = None
    categories = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter anything yet!")
                return redirect(reverse("products"))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, "products/products.html", context)


def product_info(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_info.html", context)


@login_required
def add_product(request):
    """A view to add products"""
    if not request.user.is_superuser:
        messages.error(request, "You need admin rights to access this page")
        return redirect("home")

    # form = ProductForm(request.POST, request.FILES)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect(reverse("add_product"))
        else:
            messages.error(request, "Invalid form. Try again")
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """A view to edit products"""
    if not request.user.is_superuser:
        messages.error(request, "You need admin rights to access this page")
        return redirect("home")

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully updated")
            return redirect(reverse("product_info", args=[product.id]))
        else:
            messages.error(request, "Invalid form! Please try again.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.title}")

        template = 'products/edit_a_product.html'

    context = {
        # "edit": True,
        "form": form,
        "product": product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, pk):
    """A view to delete a product"""
    if not request.user.is_superuser:
        messages.error(request, "You need admin rights to access this page")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, f"{product.title} deleted successfully")
    return redirect(reverse("products"))
