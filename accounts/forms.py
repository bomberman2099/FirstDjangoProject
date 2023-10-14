from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder':"Enter First Name"}))
    last_name = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder':"Enter Last Name"}))
    username = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder':"Enter username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"Enter email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"repeat Password"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists, please try another.'
            self.add_error('username', error_message)
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 is None:
            error_message = 'Password is required'
            self.add_error('password1', error_message)
        if len(password1) < 8 or len(password2) < 8:
            error_message = 'Passwords must have 8 characters or more'
            self.add_error('password1', error_message)
        if password1 != password2:
            error_message = "Passwords don't match"
            self.add_error('password1', error_message)
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=45, widget=forms.Textarea(attrs={'placeholder': "Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter Password"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error_message = 'Username is wrong! Try another.'
            self.add_error('username', error_message)
        else:
            password = cleaned_data.get('password')
            if not user.check_password(password):
                error_message = 'Password is wrong! Try another.'
                self.add_error('password', error_message)
        return cleaned_data


class EditYourProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'username', 'image']


