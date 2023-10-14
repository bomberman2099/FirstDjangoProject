from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=25, verbose_name="نام پدر")
    melicode = models.CharField(max_length=10, verbose_name="کد ملی")
    image = models.ImageField(upload_to="profile/images", blank=True, null=True, verbose_name="تصویر")
    username = models.CharField(default="a", max_length=150, verbose_name="نام کاربری")
    first_name = models.CharField(default="a", max_length=30, verbose_name="نام")
    last_name = models.CharField(default="a", max_length=150, verbose_name="نام خانوادگی")
    email = models.EmailField(default="a", max_length=254, verbose_name="ایمیل")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"