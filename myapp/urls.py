from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('cart/<int:id>/',views.cart_page,name='cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('billing/',views.billing,name='billing'),
]