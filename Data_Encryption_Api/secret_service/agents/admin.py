

# Register your models here.
from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "code_name", "location", "secret_mission")

admin.site.register(Agent, AgentAdmin)