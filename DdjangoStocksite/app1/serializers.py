from django.db.models import fields
from rest_framework import serializers
from app1.models import Tutorial
from .models import Quiz

class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

    def create(self,validated_data):
        return Tutorial.objects.create(**validated_data)






class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields  = ('description')
