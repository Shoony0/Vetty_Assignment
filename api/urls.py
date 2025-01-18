from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("coins/list/", views.get_coins_list, name="coins_list"),
    path("coins/categories/", views.get_coins_categories, name="coins_categories"),
    path("coins/markets/", views.get_coins_markets, name="coins_markets"),
]
