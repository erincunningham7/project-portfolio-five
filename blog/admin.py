from django.contrib import admin
from .models import Topic


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_on", "status")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status",)


admin.site.register(Topic, TopicAdmin)
