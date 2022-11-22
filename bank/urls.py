from django.urls import path
from bank import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet, basename='category')

urlpatterns = [
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
] + router.urls
