from django.urls import path
from . import views

urlpatterns = [
    path('api/messages/<int:sender>/<int:receiver>', views.list_message, name='message-detail'),
    path('api/messages/', views.list_message, name='message-list'),
    path('api/users/<int:pk>', views.list_user, name='user-detail'),
    path('api/users/', views.list_user, name='user-list'),
]