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
    # redirect_url = request.POST.get('redirect_url')
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
                request, "There was an error submitting your form. Please try again."
            )
        return redirect(reverse("product_info", args=[product_id]))
    else:
        form = UserReviewForm()
    # return redirect(redirect_url)
    context = {"product": product, "form": form}
    return render(request, "reviews/add_review.html", context)


@login_required
def update_review(request, product_id):
    """
    A view to handle updating a product review
    """
    review = get_object_or_404(UserReview, id=product_id)
    product = review.product
    form = UserReviewForm(instance=review)

    if request.method == "POST":
        user = request.user.userprofile
        if request.user.is_superuser or user == review.user:
            form = UserReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save()
                messages.success(request, "Updated review successfully!")
                return redirect("product", product.id)
            messages.error(
                request, "There was an error updating your review. Please try again."
            )
        else:
            messages.error(
                request,
                "You are forbidden from updating this review. Please login or register.",
            )

    template = "reviews/update_review.html"
    context = {"review_form": form, "review": review, "product": product}
    return render(request, template, context)


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
