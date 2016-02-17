from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView

def message_view(request):
    messages = Message.objects.all()
    context = {}
    context['messages'] = messages

    if request.method == 'POST':

        comment_body = request.POST.get('comment_body', None)
        message = request.POST.get('message', None)
        user = request.POST.get('user', None)


        print comment_body
        print message
        print user

        current_user = User.objects.get(username=user)
        current_message = Message.objects.get(title=message)

        Comment.objects.create(body = comment_body, user=current_user, message=current_message)

    return render(request, 'message.html', context)


def post_view(request):
    messages = Message.objects.all()
    context = {}
    context['messages'] = messages
    if request.method == 'POST':

        message_body = request.POST.get('message_body', None)
        title = request.POST.get('title', None)
        user = request.POST.get('user', None)

        print message_body
        print title
        print user

        current_user = User.objects.get(username=user)

        Message.objects.create(body=message_body, user=current_user, title=title)

    return render(request, 'post.html', context)

class PostView(CreateView):
    model = Message
    template_name = "post_create_form.html"
    fields = '__all__'
    context_object_name = "message"