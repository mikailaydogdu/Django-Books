from django.contrib import admin
from .models import Posts, Comment

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Posts

admin.site.register(Posts, PostsAdmin)
admin.site.register(Comment)