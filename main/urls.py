from django.conf.urls import url

from .views import MessageListView

urlpatterns = [
    
    url(r'^message/$', MessageListView.as_view()),
    
]