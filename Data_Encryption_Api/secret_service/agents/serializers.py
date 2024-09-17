from rest_framework import serializers
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('first_name', 'last_name', 'badge_no', 'code_name', 'location', 'secret_mission')