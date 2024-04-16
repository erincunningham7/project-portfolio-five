from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import UserReviewForm
from .models import UserReview
from django.urls import reverse


# Create your views here.
def reviews_list(request, product_id):
    """
    A view that handles displaying the reviews page
    """
    product_reviews = UserReview.objects.filter(product_id=product_id)
    if not product_reviews.exists():
        messages.error(request, "There are no reviews available at this time.")
        return redirect("product_info", product_id=product_id)

    product = product_reviews.first().product
    template_name = "reviews/reviews.html"
    context = {"reviews": product_reviews, "product": product}
    return render(request, template_name, context)


@login_required
def add_review(request, product_id):
    """
    A view that handles adding a product review
    """
    product = get_object_or_404(Product, id=product_id)
    user = request.user.userprofile
    if request.method == "POST":
        form = UserReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, "Added review successfully!")
        else:
            messages.error(
                request,
                "There was an error submitting your form. Please try again."
            )
        return redirect(reverse("product_info", args=[product_id]))
    else:
        form = UserReviewForm()
    context = {"product": product, "form": form}
    return render(request, "reviews/add_review.html", context)


@login_required
def update_review(request, product_id):
    """A view to update reviews"""
    user = request.user.userprofile
    review = get_object_or_404(UserReview, pk=product_id)
    product = review.product

    if not request.user.is_superuser or not user == review.user:
        messages.error(request, "You do not have the rights to access this page")
        return redirect("home")

    if request.method == "POST":
        form = UserReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review successfully updated")
            return redirect(reverse("product_info", args=[product.id]))
        else:
            messages.error(request, "Invalid form! Please try again.")
    else:
        form = UserReviewForm(instance=review)
        messages.info(request, f"You are editing {product.title}")

        template = 'reviews/update_review.html'

    context = {
        "form": form,
        "review": review,
        "product": product,
    }
    return render(request, template, context)

    # if request.method == "POST":
    #     form = UserReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Product added successfully.")
    #         return redirect(reverse("add_product"))
    #     else:
    #         messages.error(request, "Invalid form. Try again")
    # else:
    #     form = ProductForm()

    # template = "products/add_product.html"
    # context = {
    #     "form": form,
    # }

    # return render(request, template, context)


@login_required
def delete_review(request, product_id):
    """
    A view to handle deleting a product review
    """
    review = get_object_or_404(UserReview, id=product_id)
    product = review.product

    if request.method == "POST":
        user = request.user.userprofile
        if request.user.is_superuser or user == review.user:
            try:
                review.delete()
                messages.success(request, "Deleted review successfully!")
            except ObjectDoesNotExist:
                messages.error(request, "This review does not exist.")

    return redirect(reverse("product_info", args=[product_id]))

    template = "reviews/delete_review.html"
    context = {
        "review": review,
        "product": product,
    }

    return render(request, template, context)
