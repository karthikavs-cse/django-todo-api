from django.contrib import admin
from .models import Task, User, Item

admin.site.register(Task)
admin.site.register(User)
admin.site.register(Item)