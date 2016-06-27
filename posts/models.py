from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from imagekit.models import ProcessedImageField
from imagekit.processors import Resize
# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50)
  created_date = models.DateTimeField(auto_now_add=True, editable=False)
  modified_date = models.DateTimeField(auto_now=True)
  content1 = models.TextField(default='', blank=True)
  photo1 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  content2 = models.TextField(default='', blank=True)
  photo2 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  content3 = models.TextField(default='', blank=True)
  photo3 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  content4 = models.TextField(default='', blank=True)
  photo4 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  content5 = models.TextField(default='', blank=True)
  photo5 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  tags = models.CharField(max_length=200, default='', blank=True)

  def __str__(self):
    return self.title

class Project(models.Model):
  name = models.CharField(max_length=50)
  tech_list = models.TextField(default='', blank=True)
  created_date = models.DateTimeField(auto_now_add=True, editable=False)
  modified_date = models.DateTimeField(auto_now=True)
  content1 = models.TextField(default='', blank=True)
  content2 = models.TextField(default='', blank=True)
  content3 = models.TextField(default='', blank=True)
  content4 = models.TextField(default='', blank=True)
  photo1 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  photo2 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  photo3 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  photo4 = ProcessedImageField(blank=True, processors=[Resize(800, 500)])
  link = models.CharField(max_length=100, default='', blank=True)
  categories = models.CharField(max_length=200, default='', blank=True)

  def __str__(self):
    return self.name


