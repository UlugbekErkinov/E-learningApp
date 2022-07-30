from django.urls import path

from . import views



urlpatterns = [
    path('category/top', views.CategoryTopListView.as_view()),
    path('category/most', views.CategoryMostWatchedListView.as_view()),
    path('course/continue', views.CourseListContinueWatchView.as_view()),
    path('course/topteacher', views.CourseListTopTeacherView.as_view()),
    path('course/other', views.CourseListOtherWatchView.as_view()),
    path('course/comment', views.CourseListAPIView.as_view()),
    
]