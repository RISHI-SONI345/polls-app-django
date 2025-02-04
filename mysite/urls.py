from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # ✅ Login ke liye
    TokenRefreshView      # ✅ Expired token refresh karne ke liye
)

urlpatterns = [
    path("polls/", include("polls.urls")),  
    path("admin/", admin.site.urls),
    path("api/token",TokenObtainPairView.as_view(),name='token obtain_pair'),
    path("api/token/refresh",TokenRefreshView.as_view(),name='token_refresh')
]
