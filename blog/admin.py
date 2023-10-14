from django.contrib import admin
from . import models

class FilterByTitle(admin.SimpleListFilter):
    title = " کلید های پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ('batman', "بتمن"),
            ('bomberman', "بومبرمن"),
            ("hadad", "حداد"),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())

class CommentsInline(admin.TabularInline):
    model = models.Comments
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "get_short_body", "showimage")
    list_filter = ('author', FilterByTitle)
    search_fields = ("title", 'body')
    inlines = (CommentsInline,)
    def get_short_body(self, obj):
        return ' '.join(obj.body.split()[:10]) + '...'
    get_short_body.short_description = "متن"

admin.site.register(models.Category)
admin.site.register(models.Comments)
admin.site.register(models.ContactUs)
admin.site.register(models.Like)

