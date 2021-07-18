from rest_framework import serializers
from app1.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

    def create(sef,validated_data):
        return Tutorial.objects.create(**validated_data)
    
    