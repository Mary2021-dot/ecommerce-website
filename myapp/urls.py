from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from myapp import views as user_views

urlpatterns=[
    path('',views.index,name="index"),
    path('register/', user_views.register, name='register'),
  
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('product/<int:product_id>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]