from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView

from .models import Message, Comment

# Create your views here.


class MessageListView(ListView):
    model = Message
    template_name = "message.html"
    context_object_name = "message_list"