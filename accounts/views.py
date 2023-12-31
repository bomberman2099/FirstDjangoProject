from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, EditYourProfile
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.models import ContactUs
from django.urls import reverse_lazy
from .models import Profile


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create a new User object with the form data
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            user.save()

            # Automatically log in the user after registration
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                User.objects.get(username=username)
                authenticated_user = authenticate(request, username=username, password=password)

                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect("/")
                else:
                    raise User.DoesNotExist
            except User.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def EditProfile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=user)

    form = EditYourProfile(instance=user)

    if request.method == 'POST':
        form = EditYourProfile(data=request.POST, files=request.FILES, instance=profile)

        if form.is_valid():
            form.save()

    return render(request, 'accounts/editProfile.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')


# ------------------------------------------


class UserList(UserPassesTestMixin, ListView):
    queryset = User.objects.all()
    template_name = "accounts/keepclean.html"

    def test_func(self):
        return self.request.user.is_superuser


class MessageUpdateView(UserPassesTestMixin, ListView):
    model = ContactUs
    template_name = 'accounts/MessageUpdateView.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        print(self.request.user)
        return context

    def test_func(self):
        return self.request.user.is_superuser


class MessageDetailView(UserPassesTestMixin, UpdateView):
    model = ContactUs
    fields = ("__all__")
    template_name = 'accounts/message_detail.html'
    context_object_name = 'message'
    success_url = reverse_lazy('accounts:message-update')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        print(self.request.user)
        return context

    def test_func(self):
        return self.request.user.is_superuser


class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = ContactUs
    success_url = reverse_lazy('accounts:message-update')
    template_name = 'accounts/contactus_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        print(self.request.user)
        return context

    def test_func(self):
        return self.request.user.is_superuser
