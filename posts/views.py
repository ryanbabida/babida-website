from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
import re

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = "posts/index.html"


class ProjectsView(generic.ListView):
  template_name = "posts/projects.html"
  context_object_name = 'projects_list'

  def get_queryset(self):
    return Project.objects.filter(modified_date__lte=timezone.now()
      ).order_by('-modified_date')

  def get_categories(self):
    categories_list = list()
    project_list = Project.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for project in project_list:
      categories = re.split(' ', project.categories)
      for cat in categories:
        if cat not in categories_list:
          categories_list.append(cat)
    return categories_list


class CategoriesView(generic.ListView):
  template_name = "posts/projects.html"
  context_object_name = 'projects_list'

  def get_queryset(self):
    category = self.kwargs['category']
    return Project.objects.filter(categories__contains=category).order_by('-modified_date')

  def get_categories(self):
    categories_list = list()
    project_list = Project.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for project in project_list:
      categories = re.split(' ', project.categories)
      for cat in categories:
        if cat not in categories_list:
          categories_list.append(cat)
    return categories_list


class BlogView(generic.ListView):
  template_name = "posts/blog.html"
  context_object_name = 'latest_post_list'

  def get_queryset(self):
    return Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')

  def get_tag_list(self):
    tag_list = list()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      tags = re.split(' ', post.tags)
      for tag in tags:
        if tag not in tag_list:
          tag_list.append(tag)
    return tag_list

  def get_year_month_data(self):
    archive_data = dict()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      if post.created_date.year not in archive_data:
          archive_data[post.created_date.year] = []
          archive_data[post.created_date.year].append(post.created_date.month)
      elif post.created_date.month not in archive_data[post.created_date.year]:
          archive_data[post.created_date.year].append(post.created_date.month)
    return archive_data


class ArchiveYearView(generic.ListView):
  template_name = "posts/blog.html"
  context_object_name = 'latest_post_list'

  def get_queryset(self):
    year = self.kwargs['year']
    post_list = Post.objects.filter(created_date__year=year).order_by('-created_date')
    return post_list

  def get_tag_list(self):
    tag_list = list()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      tags = re.split(' ', post.tags)
      for tag in tags:
        if tag not in tag_list:
          tag_list.append(tag)
    return tag_list

  def get_year_month_data(self):
    archive_data = dict()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      if post.created_date.year not in archive_data:
          archive_data[post.created_date.year] = []
          archive_data[post.created_date.year].append(post.created_date.month)
      elif post.created_date.month not in archive_data[post.created_date.year]:
          archive_data[post.created_date.year].append(post.created_date.month)
    return archive_data


class ArchiveMonthView(generic.ListView):
  context_object_name = 'latest_post_list'
  template_name = "posts/blog.html"

  def get_queryset(self):
    year = self.kwargs['year']
    month = self.kwargs['month']
    post_list = Post.objects.filter(created_date__year=year).filter(created_date__month=month).order_by('-created_date')
    return post_list

  def get_tag_list(self):
    tag_list = list()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      tags = re.split(' ', post.tags)
      for tag in tags:
        if tag not in tag_list:
          tag_list.append(tag)
    return tag_list

  def get_year_month_data(self):
    archive_data = dict()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      if post.created_date.year not in archive_data:
          archive_data[post.created_date.year] = []
          archive_data[post.created_date.year].append(post.created_date.month)
      elif post.created_date.month not in archive_data[post.created_date.year]:
          archive_data[post.created_date.year].append(post.created_date.month)
    return archive_data


class TagView(generic.ListView):
  template_name = "posts/blog.html"
  context_object_name = 'latest_post_list'

  def get_queryset(self):
    tag = self.kwargs['tag']
    return Post.objects.filter(tags__contains=tag).order_by('-created_date')

  def get_tag_list(self):
    tag_list = list()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      tags = re.split(' ', post.tags)
      for tag in tags:
        if tag not in tag_list:
          tag_list.append(tag)
    return tag_list

  def get_year_month_data(self):
    archive_data = dict()
    post_list = Post.objects.filter(created_date__lte=timezone.now()
      ).order_by('-created_date')
    for post in post_list:
      if post.created_date.year not in archive_data:
          archive_data[post.created_date.year] = []
          archive_data[post.created_date.year].append(post.created_date.month)
      elif post.created_date.month not in archive_data[post.created_date.year]:
          archive_data[post.created_date.year].append(post.created_date.month)
    return archive_data


class ContactView(generic.TemplateView):
  template_name = "posts/contact.html"
 