from blog.models import Article,Category

def art(request):
    context = Article.objects.all().order_by("-updated",)
    categories = Category.objects.all()
    return {"articles": context, "category": categories}
