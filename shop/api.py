from django.db.models import Avg, Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Brand, Category, Product, Review
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer, ReviewSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related("category", "brand").annotate(avg_rating=Avg("reviews__rating"))

    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        search = p.get("search")
        if search:
            qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
        for key, field in [("category", "category_id"), ("brand", "brand_id")]:
            value = p.get(key)
            if value and value.isdigit():
                qs = qs.filter(**{field: value})
        for key, op in [("min_price", "gte"), ("max_price", "lte"), ("min_rating", "avg_rating__gte")]:
            value = p.get(key)
            if value:
                field = {"min_price": "price__gte", "max_price": "price__lte", "min_rating": "avg_rating__gte"}[key]
                try:
                    qs = qs.filter(**{field: value})
                except (ValueError, TypeError):
                    pass
        return qs

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("user", "product").all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "head", "options"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
