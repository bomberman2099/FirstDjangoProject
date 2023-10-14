from django.db import models
from django.contrib.auth.models import User, timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

# Many To Many
# Article to User
# Many To One
# One To One
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now=True, verbose_name="تاریخ ایجاد")
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:categories", kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="نویسنده")
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="دسته‌بندی")
    title = models.CharField(max_length=70, unique=True, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to='images/articles', verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        ordering = ("created",)
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={'slug': self.slug})

    def showimage(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="60px">')
        return format_html('<h3 style="color: red" >تصویر موجود نیست</h3>')

    showimage.short_description = "تصاویر"
    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True, verbose_name="پاسخ به")
    body = models.TextField(verbose_name="متن")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f'{self.user}- {self.body[:30]}'

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="likes", verbose_name="کاربر")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="Likes", verbose_name="مقاله")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ("created_at",)
class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="کاربر")
    title = models.CharField(max_length=35, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")
    age = models.IntegerField(default=0, verbose_name="سن")
    email = models.EmailField(verbose_name="ایمیل")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title}-{self.text[:45]}"

    class Meta:
        verbose_name = "بخش ارتباط با ما"
        verbose_name_plural = "بخش‌های ارتباط با ما"
        ordering = ("created_at",)