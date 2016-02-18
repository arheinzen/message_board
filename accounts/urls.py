from django.conf.urls import url

from .views import SignUp

urlpatterns = [
    
    url(r'^login/$','django.contrib.auth.views.login', name='login', kwargs={'template_name': 'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/main/message'}),
    url(r'^signup/', SignUp.as_view(success_url='/accounts/login/')),

]