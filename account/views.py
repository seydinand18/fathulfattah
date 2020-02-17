from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from . import forms


def login_view(request):
    message = ""
    form = forms.LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/member/", {'succes': message})
        else:
            message = "login et/ou mot de passe incorrect"
    return render(request, 'account/pages/login.html', {'form': form, 'error': message})


"""
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'utilisateurs/page/register.html', {'form': form})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
"""