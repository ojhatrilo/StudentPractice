from django.contrib import admin
from .models import Data,Department,Department_Section
# Register your models here.

admin.site.register(Department)
admin.site.register(Department_Section)
admin.site.register(Data)