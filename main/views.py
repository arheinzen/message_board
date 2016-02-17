from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from .models import Message, Comment

# Create your views here.


class MessageListView(ListView):
    model = Message
    template_name = "message.html"
    context_object_name = "message_list"
    

class CommentCreateView(CreateView):
    model = Comment
    template_name = "comment_create_form.html"
    fields = ['comments', 'user', 'messages']
    context_object_name = "comment_list"
    

class PostView(CreateView):
    model = Message
    template_name = "post_create_form.html"
    fields = '__all__'
    context_object_name = "message"