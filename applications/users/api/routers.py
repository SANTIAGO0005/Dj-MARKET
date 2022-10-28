from rest_framework.routers import DefaultRouter
from ...users.api.views.viewSets import UserViewSet

router = DefaultRouter()

router.register(r'User',UserViewSet)

urlpatterns = router.urls