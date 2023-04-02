from django.contrib import admin
from .models import Article
from .models import Category
from .models import Image
from .models import UserDescription
from .models import BlogInfo
from .models import Tag
from .models import Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(UserDescription)
admin.site.register(BlogInfo)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)