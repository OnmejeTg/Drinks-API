from django.urls import path
from bank import views
urlpatterns = [
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
    path('category/', views.CategoryModelViewSet.as_view(), name='category')
]
