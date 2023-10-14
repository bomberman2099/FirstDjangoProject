from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('register/', views.register,name='register'),
    path('editprofile/', views.EditProfile,name='editProfile'),
    path('users/', views.UserList.as_view(),name='users'),
    path('messages/', views.MessageUpdateView.as_view(), name='message-update'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    path('messages/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message-delete'),

]

