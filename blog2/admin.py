from django.contrib import admin
from blog2.models import Tag, Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields ={"slug":("title",)}

  list_display = ('summary','content')


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)