from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from .forms import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
