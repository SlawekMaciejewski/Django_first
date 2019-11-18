from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_date', 'published_date',)
    list_filter = ('author', 'created_date',)
    date_hierarchy = 'published_date'
    raw_id_fields = ('author',)

admin.site.register(Post, PostAdmin)
