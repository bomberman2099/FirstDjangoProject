from django import forms
from django.forms import TextInput, Textarea, EmailInput
from django.core.validators import ValidationError

from blog.models import ContactUs, Article


# class ContactUs(forms.Form):
#     BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
#
#     for year in range(1983, 2025):
#         BIRTH_YEAR_CHOICES.append(str(year))
#     FAVORITE_COLORS_CHOICES = [
#         ("green", "Green:"),
#         ("black", "Black:"),
#         ("blue", "Blue:"),
#     ]
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "form-control"}))
#     colors = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
#     content = forms.CharField(max_length=50, label="your messages content")
#     text = forms.CharField(max_length=500, label="your messages")
#
#
#
#     def clean(self):
#         content = self.cleaned_data.get("content")
#         text = self.cleaned_data.get("text")
#         if content == text:
#             raise ValidationError("text and content are same", code="text_content_same")





class MessageForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        exclude = ("crreated_at", 'user')

        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg',
                                      'style': 'border-radius: 10px; padding: 10px 15px; font-size: 13px;',
                                      'placeholder': 'Enter title'}),
            'text': Textarea(
                attrs={'class': 'form-control', 'style': 'border-radius: 10px; padding: 10px; font-size: 12px;',
                       'placeholder': 'Enter text'}),
            'age': TextInput(
                attrs={'class': 'form-control', 'style': 'border-radius: 10px; padding: 10px; font-size: 12px;',
                       'placeholder': 'Enter age'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'style': 'border-radius: 10px; padding: 10px; font-size: 12px;',
                       'placeholder': 'Enter email'}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'category', 'title', 'body', 'image']



