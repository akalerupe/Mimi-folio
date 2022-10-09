from django.contrib import admin
from .models import Profile,Tag, Post
# Register your models here.
admin.site.register(Profile)
admin.site.register(Tag)
# admin.site.register(Post)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    model:Post
    list_display= (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter=(
        "published",
        "publish_date"
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True
