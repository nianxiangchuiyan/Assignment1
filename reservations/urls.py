from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import ProfileDetail

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),

    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', ProfileDetail.as_view(), name='profile_detail'),
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/reserve/', views.make_reservation, name='make_reservation'),
    path('allrooms/', views.all_rooms_view, name='all_rooms'),

]
