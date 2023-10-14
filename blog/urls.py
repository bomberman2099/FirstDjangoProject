from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('detail/<slug:slug>/', views.blogs_detail, name='details'),
    path('categories/<slug:slug>/', views.categories, name='categories'),
    path('search/', views.search, name='search_articles'),
    path('contactUs/', views.contacts, name='contactUs'),
    path('detail/<slug:slug>/like/<int:Pk>', views.Likes, name='Like'),
    path('test/', views.test, name='test'),

]