from rest_framework.routers import DefaultRouter
from ...producto.api.views.mark_viewSet import MarkViewSet
from ...producto.api.views.provider_viewSet import ProviderViewSet
from ...producto.api.views.product_viewSet import ProductViewSet
router = DefaultRouter()
router.register(r'Mark',MarkViewSet)
router.register(r'Provider',ProviderViewSet)
router.register(r'Product',ProductViewSet)

urlpatterns = router.urls