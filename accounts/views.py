from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import CreateUserForm

# Create your views here.

class SignUp(CreateView):
    form_class = CreateUserForm
    template_name = 'sign_up.html'