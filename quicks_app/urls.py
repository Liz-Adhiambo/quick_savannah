from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    path('signup/', views.google_login, name='google_login'),
    path('user/signup/', views.signup, name='signup'),
    path('user/login/', views.login_view, name='login_view'),
]