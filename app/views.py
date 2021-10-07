from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from app.form import EditorForm, EditorModel


def main_page(request):
    return render(request, "index.html")


def login_user(request):
    user_name = request.POST.get("u1")
    password = request.POST.get("u2")
    user = auth.authenticate(username=user_name,password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, "home.html", {"form":EditorForm()})
    else:
        messages.error(request, 'Invalid Credentials')
        return render('main')


def save(request):
    ef = EditorForm(request.POST)
    if ef.is_valid():
        ef.save()
    return redirect('main')