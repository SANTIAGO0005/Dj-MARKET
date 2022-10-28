from rest_framework.routers import DefaultRouter

from ...caja.api.viewSets import CloseBoxViewSet

router = DefaultRouter()

router.register('Box', CloseBoxViewSet,basename='CloseBox')

urlpatterns = router.urls