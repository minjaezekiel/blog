from django.contrib import admin
from .models import Post

#models Registry
#By Ezekiel Minja

#Post model registry
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    search_fields = ('name')
    list_filter = ('title','created')
