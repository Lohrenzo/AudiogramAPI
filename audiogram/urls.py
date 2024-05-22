from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenObtainPairView,
)

from .views import CustomTokenObtainPairView

# from django.urls import re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("audiogramAPI.urls")),
    path("account/", include("account.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # path('api/token/blacklist', TokenBlacklistView.as_view(), name='token_blacklist'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
