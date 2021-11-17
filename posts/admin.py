from django.contrib import admin
from .models import Post
from django.utils.html import format_html
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude=()
    list_display=('name_post','approve')
    def approve(self, obj):
        return format_html("<button class='btn-approve'>Duyệt</button>")

admin.site.register(Post,PostAdmin)