from distutils.command.upload import upload
from django.db import models
from helpers.models import BaseModel
from common.models import User
from django.db.models import Avg



# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_top = models.BooleanField(default=False)
    most_watched = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Course(BaseModel):
    teacher = models.ForeignKey(User, related_name='teachers', on_delete=models.CASCADE)
    subject = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to = 'course/')
    video_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name='students_joined', blank=True)
    rating = models.PositiveIntegerField()
    view_count = models.PositiveIntegerField()
    is_continue = models.BooleanField()
    is_other = models.BooleanField()
    top_teacher = models.BooleanField(default=True)
    


    class Meta:
        ordering = ('-created',)

    # def save(self, *args, **kwargs):
        # if not self.slug:
            # self.slug = slugify(self.title)
        # super(Course, self).save(*args, **kwargs)

    def Avg(self):
        # all_ratings = map(lambda x: x.rating, self.reviews.all())
        # return np.mean(all_ratings)
        return self.reviews.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.title

class Comment(BaseModel):
    content = models.TextField()
    rating = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
