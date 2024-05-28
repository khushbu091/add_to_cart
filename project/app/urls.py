from django.urls import *
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/',register,name='register'),
    path('showdata/',showdata,name='showdata'),
    path("addtocard/<int:pk>",addtocard,name='addtocard'), 
    # path("addtocart/",cart,name="cart"),
    path('cart_item/',cart_item,name='cart_item')
]