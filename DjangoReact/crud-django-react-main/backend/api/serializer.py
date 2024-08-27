from rest_framework.serializers import ModelSerializer
from .models import Students

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'