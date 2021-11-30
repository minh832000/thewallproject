from django.contrib import admin
from .models import Post, Post_apply
from django.utils.html import format_html
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude=()
    list_display=('name_post','confirm')
    actions=['approve_post', 'cancel_approve']
    def approve_post(self, request, queryset):
        queryset.update(confirm=True)
    def cancel_approve(self, request, queryset):
        queryset.update(confirm=False)

admin.site.register(Post,PostAdmin)
admin.site.register(Post_apply)