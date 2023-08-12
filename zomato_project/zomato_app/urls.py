# zomato_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('menu/', views.menu, name='menu'),
    path('orders/', views.order_list, name='order_list'),

    path('add_dish/', views.add_dish, name='add_dish'),
    path('place_order/', views.place_order, name='place_order'),
    path('update_dish_availability/<int:dish_id>/', views.update_dish_availability, name='update_dish_availability'),

   
    path('update_dish_availability/<int:dish_id>/', views.update_dish_availability, name='update_dish_availability'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    # chatbot url ;
    path('chatbot/', views.chatbot, name='chatbot'),
    path('dish_detail/<int:dish_id>/', views.dish_detail, name='dish_detail'),

     

]
