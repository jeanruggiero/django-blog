from django.contrib import admin
from myblog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]




