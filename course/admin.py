from django.contrib import admin
from .models import Category, Course, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ordering = ('is_top', 'most_watched')
    list_filter = ('title', 'most_watched')
    list_display=('title','is_top', 'most_watched')
    search_fields = ("title",'slug')
    

admin.site.register(Category, CategoryAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=('title','teacher', 'rating')
    ordering = ('view_count', 'rating')
    list_filter = ('is_continue', 'is_other')
    search_fields = ("title",'slug')


admin.site.register(Course, CourseAdmin)

admin.site.register(Comment)
