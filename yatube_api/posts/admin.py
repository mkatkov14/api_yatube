from django.contrib import admin

from .models import Group, Post

admin.site.register(Post)
admin.site.register(Group)
