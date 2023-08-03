from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),
    path('record/<int:pk>', views.customerRecord, name = 'record'),
    path('delete_record/<int:pk>', views.deleteRecord, name = 'delete_record'),
    path('add_record', views.addRecord, name = 'add_record'),
]
