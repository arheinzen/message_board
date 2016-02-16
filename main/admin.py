from django.contrib import admin
from .models import Comment, Message

# Register your models here.


admin.site.register(Comment)
admin.site.register(Message)