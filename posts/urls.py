from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name="index"),
  url(r'^projects/$', views.ProjectsView.as_view(), name="projects"),
  url(r'^projects/(?P<category>[\w\-]+)$', views.CategoriesView.as_view(), name="categories"),
  url(r'blog/$', views.BlogView.as_view(), name="blog"),
  url(r'blog/tags/(?P<tag>[\w\-]+)$', views.TagView.as_view(), name="tag"),
  url(r'blog/(?P<year>[0-9]{4})$', views.ArchiveYearView.as_view(), name="year"),
  url(r'blog/(?P<year>[0-9]{4})/(?P<month>[0-9])/$', views.ArchiveMonthView.as_view(), name="month"),
  url(r'contact/$', views.ContactView.as_view(), name="contact"),
]