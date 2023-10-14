from django.shortcuts import render
from blog.models import Article, Category
from django.urls import reverse


def home(request):
    if request.user.is_authenticated == True:
        context = {
            "user1": request.user.first_name,

            "articles2": Article.objects.all().order_by("-updated",)[:3],
        } 
        return render(request, 'home/index.html', context)
    
    else:
        context = {
        "user1": "Guest(no login)",
        "articles2": Article.objects.all().order_by("-updated",)[:3],
        }  
        return render(request, 'home/index.html', context)


def sidebar(request):
    data = {"name": "amir hossein"}
    return render(request, "includes/sidebar.html", context=data)
