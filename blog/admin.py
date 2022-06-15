from django.contrib import admin

from blog.models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "author",
        "title",
        "writing",
        "is_public",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["pk", "author", "title", "writing"]
    list_filter = ["created_at", "is_public"]
    search_fields = ["author", "title", "writing"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_display_links = ["name", "description"]
    search_fields = ["name", "description"]
