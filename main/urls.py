from django.conf.urls import url

from .views import MessageListView, CommentCreateView, PostView

urlpatterns = [
    
    url(r'^message/$', MessageListView.as_view()),
    url(r'^post/$', PostView.as_view(success_url="/main/message/")),
    url(r'^comment/$', CommentCreateView.as_view(success_url="/main/message/")),
    
]