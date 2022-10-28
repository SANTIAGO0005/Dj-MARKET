from rest_framework.routers import DefaultRouter
from ...venta.api.viewSets.sales_viewSet import SaleViewSet
from ...venta.api.viewSets.salesDetails_viewSet import SaleDetailViewSet
from ...venta.api.viewSets.carshop_viewSet import CarShopViewSet

router = DefaultRouter()

router.register(r'Sale',SaleViewSet)
router.register(r'SaleDetail',SaleDetailViewSet)
router.register(r'CarShop',CarShopViewSet)

urlpatterns = router.urls