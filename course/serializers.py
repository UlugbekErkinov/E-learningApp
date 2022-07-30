from rest_framework import serializers
from .models import Category, Course, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','subject','comments', 'rating']