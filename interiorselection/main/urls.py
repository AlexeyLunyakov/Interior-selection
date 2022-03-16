from django.urls import path
from . import views

urlpatterns = [
    path('home', views.mainpg, name='home'),
    path('contacts', views.about, name='contacts'),
    path('stock', views.stock, name='stock'),
    path('faqs', views.faqs, name='faqs'),
    path('displacement', views.DisplacementView.as_view(), name='displacement'),
    path('cabinets', views.CabinetsView.as_view(), name='cabinets'),
    path('create_room', views.CreateRoomView.as_view(), name='create_room'),
    path('room/<int:id>/', views.RoomView.as_view(), name='room'),
    path('room/<int:id>/update', views.UpdateRoomView.as_view(), name='update_room'),
    path('room/<int:id>/delete', views.DeleteRoomView.as_view(), name='delete_room'),
]
