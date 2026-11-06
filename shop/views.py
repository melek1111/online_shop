from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import RegisterForm, ReviewForm
from .models import Brand, Cart, CartItem, Category, Product, Review

def home(request):
    products = Product.objects.select_related("category", "brand").annotate(avg_rating=Avg("reviews__rating"))
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "")
    brand_id = request.GET.get("brand", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")
    min_rating = request.GET.get("rating", "")

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id.isdigit():
        products = products.filter(category_id=category_id)
    if brand_id.isdigit():
        products = products.filter(brand_id=brand_id)
    try:
        if min_price: products = products.filter(price__gte=Decimal(min_price))
        if max_price: products = products.filter(price__lte=Decimal(max_price))
    except Exception:
        messages.warning(request, "ფასის ფილტრში არასწორი მნიშვნელობაა.")
    if min_rating in {"1", "2", "3", "4", "5"}:
        products = products.filter(avg_rating__gte=int(min_rating))
    return render(request, "shop/home.html", {
        "products": products, "categories": Category.objects.all(), "brands": Brand.objects.all(),
        "filters": request.GET,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related("category", "brand"), pk=pk)
    reviews = product.reviews.select_related("user")
    form = ReviewForm()
    return render(request, "shop/product_detail.html", {"product": product, "reviews": reviews, "form": form})

@login_required
@require_POST
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        Review.objects.update_or_create(
            product=product, user=request.user,
            defaults={"rating": form.cleaned_data["rating"], "comment": form.cleaned_data["comment"]}
        )
        messages.success(request, "შეფასება შენახულია.")
    else:
        messages.error(request, "შეფასების ფორმა სწორად შეავსეთ.")
    return redirect("product_detail", pk=pk)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ანგარიში წარმატებით შეიქმნა.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "shop/register.html", {"form": form})

@login_required
@require_POST
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.stock < 1:
        messages.error(request, "პროდუქტი მარაგში აღარ არის.")
        return redirect(request.META.get("HTTP_REFERER", "home"))
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={"quantity": 1})
    if not created and item.quantity < product.stock:
        item.quantity += 1
        item.save()
    elif not created:
        messages.warning(request, "მარაგში არსებული მაქსიმალური რაოდენობა უკვე კალათაშია.")
    return redirect("cart")

@login_required
def cart(request):
    cart_obj, _ = Cart.objects.get_or_create(user=request.user)
    items = cart_obj.items.select_related("product", "product__brand")
    return render(request, "shop/cart.html", {"cart": cart_obj, "items": items})

@login_required
@require_POST
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    action = request.POST.get("action")
    if action == "increase" and cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
    elif action == "decrease":
        cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect("cart")

@login_required
@require_POST
def remove_cart_item(request, item_id):
    get_object_or_404(CartItem, pk=item_id, cart__user=request.user).delete()
    messages.info(request, "პროდუქტი კალათიდან წაიშალა.")
    return redirect("cart")
