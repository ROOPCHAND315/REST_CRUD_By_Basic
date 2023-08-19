from rest_framework import serializers
from .models import StudensModel
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudensModel
        fields=['id','name','roll','city']