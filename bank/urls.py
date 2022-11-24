from django.urls import path
from bank import views
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet, basename='category')
router.register(r'transactions', views.TransactionModelViewSet, basename='transaction')

urlpatterns = [
    path('login/', obtain_auth_token, name='obtain-auth-token'),
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
] + router.urls
