from rest_framework.routers import DefaultRouter
from .api import BrandViewSet, CategoryViewSet, ProductViewSet, ReviewViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="api-products")
router.register("categories", CategoryViewSet)
router.register("brands", BrandViewSet)
router.register("reviews", ReviewViewSet)
urlpatterns = router.urls
