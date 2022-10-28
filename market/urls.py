"""
Proyecto Final

"""

from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from applications.users.api.views.login_viewSet import Logout, Login

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API",
      default_version='v1',
      description="Documentacion publica de API de market",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cifuentess938@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    re_path('Home/', include('applications.home.urls')),
    # users app
    re_path('', include('applications.users.urls')),
    # producto app
    re_path('Producto/', include('applications.producto.urls')),
    # venta app
    re_path('Ventas/', include('applications.venta.urls')),
    # caja app
    re_path('Caja/', include('applications.caja.urls')),

    # ***************url rest**********************
    #path('home/', include('applications.home.api.routers')),
    # users app
    path('logout/',Logout.as_view(),name = 'logout'),
    path('login/',Login.as_view(),name ='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user', include('applications.users.api.routers')),
    # producto app
    path('products/', include('applications.producto.api.routers')),
    # venta app
    path('sales/', include('applications.venta.api.routers')),
    # caja app
    path('box/', include('applications.caja.api.routers')),
]







