from django.urls import path
from sweets import views

urlpatterns = [
    path('sweets/', views.sweet_list),
    path('sweets/<int:pk>/', views.sweet_detail),
]