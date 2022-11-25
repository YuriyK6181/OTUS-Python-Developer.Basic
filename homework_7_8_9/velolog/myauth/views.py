from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)


@login_required
def top_secret_info_view(request):
    return HttpResponse("Some restricted information: ...")


class MyProfileView(TemplateView):
    template_name = "myauth/my.html"


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:my")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("myauth:my")
