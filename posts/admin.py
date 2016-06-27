from django.contrib import admin
from .models import *
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "modified_date", "created_date"]
	list_display_links = ["title", "modified_date", "created_date"]
	list_filter = ["title", "modified_date", "created_date"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post

class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ["name", "modified_date", "created_date"]
	list_display_links = ["name", "modified_date", "created_date"]
	list_filter = ["name", "modified_date", "created_date"]

	search_fields = ["name", "content"]
	class Meta:
		model = Project

admin.site.register(Post, PostModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
