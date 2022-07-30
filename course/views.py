from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import BasicAuthentication
# from django.shortcuts import get_object_or_404
from .models import Category, Course, Comment
from django.db.models import Sum
# from .permissions import IsEnrolled
from .serializers import CategorySerializer, CourseSerializer, CourseCommentSerializer
from django.db.models import Count
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import action

# Create your views here.


class CategoryTopListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_top=True)[:2]
    serializer_class = CategorySerializer

class CategoryMostWatchedListView(generics.ListAPIView):
    queryset = Category.objects.filter(most_watched=True)[:2]
    serializer_class = CategorySerializer

class CourseListRatingView(generics.ListAPIView):
    queryset = Course.objects.filter(rating=True)[:2]
    serializer_class = CourseSerializer

class CourseListTopTeacherView(generics.ListAPIView):
    queryset = Course.objects.filter(top_teacher=True)[:2]
    serializer_class = CourseSerializer

class CourseListContinueWatchView(generics.ListAPIView):
    queryset = Course.objects.filter(is_continue=True)[:2]
    serializer_class = CourseSerializer

class CourseListOtherWatchView(generics.ListAPIView):
    queryset = Course.objects.filter(is_other=True)[:2]
    serializer_class = CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.annotate(comment_count=Count('comments'), rate = Sum('comments__rating'))
    serializer_class = CourseCommentSerializer
    





    


