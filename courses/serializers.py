from rest_framework import serializers
from . import models

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'language', 'price')
