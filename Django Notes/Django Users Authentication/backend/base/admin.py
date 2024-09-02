from django.contrib import admin
from . import models
from django.contrib.auth.models import User,Group
# Register your models here.
# class Admin(admin.ModelAdmin):
#     list_display = ("name",)

admin.site.register(models.student)

# admin.site.unregister(User)
# admin.site.unregister(Group)


