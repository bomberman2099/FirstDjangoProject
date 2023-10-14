from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comments, ContactUs, Like
from django.core.paginator import Paginator
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# class MyDetailView(DetailView):
#     model = Article
#     template_name = "blog/post-details.html"
#     context_object_name = "artic"
#
#     def post(self, request, *args, **kwargs):
#         parent_id = request.POST.get('parent_id')
#         body = request.POST.get('body')
#         article = self.get_object()
#         Comments.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
#         return HttpResponseRedirect(reverse('blog/post-details.html', args=[article.slug]))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_count'] = self.object.comments.count()
    #     context['title'] = "post details"
    #     return context



def blogs_detail(request, slug):
    context = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comments.objects.create(body=body, article=context, user= request.user, parent_id=parent_id)

    comment_count = context.comments.count()

    if not request.user.is_anonymous:
        if request.user.likes.filter(article__slug=slug, user_id=request.user.id).exists():
            liked = True
            print(1)
        else:
            liked = False



    return render(request, "blog/post-details.html", {'comment_count':comment_count, "artic": context, "title": "post details","is_Liked": liked})

def blogs(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {"articles": objects_list, "title": 'blogs'})


# class ArticleListView(ListView):
#     model = Article
#     paginate_by = 3
#     context_object_name = 'articles'
#


def categories(request, slug=None):
    categorys = get_object_or_404(Category, slug=slug)
    articles = categorys.articles.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"categorys": categorys, "articles": objects_list, "title": 'categories'})





def Likes(request, slug, Pk):
    try:
        Likes = Like.objects.get(article__slug=slug, user_id=request.user.id)
        Likes.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(article_id=Pk, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"articles": objects_list, "title": 'searching'})


def contacts(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)       # pass request.POST daden be form
        if form.is_valid():
            # title = form.cleaned_data["title"] # cleaned_data accesing to the thing that in form with key and value
            # text = form.cleaned_data['text']
            # email = form.cleaned_data["email"]
            # ContactUs.objects.create(title=title, text=text, email=email)
            the_item_that_WILL_send_to_dataBASE_WE_acces_TO_THAT_WITH_THIS_VARIABLE = form.save()
            the_item_that_WILL_send_to_dataBASE_WE_acces_TO_THAT_WITH_THIS_VARIABLE.user = request.user
            form.save()
    else:                                           # if get error The bottom line of this line will show the errors
        form = MessageForm()
    return render(request, 'blog/contactUs.html', {"form": form, "title": "contactus"})

def test(request):
    return JsonResponse({'response': 'Liked'})

