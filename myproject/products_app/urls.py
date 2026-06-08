from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('about/contacts/', contacts_view, name='contacts'),
    path('about/how-to-find/', how_to_find_view, name='how_to_find'),
    path('products/', products_view, name='products'),
    path('products/categories/', categories_view, name='categories'),
    path('products/all/', all_products_view, name='all_products'),
    path('cart/', cart_view, name='cart'),
]
