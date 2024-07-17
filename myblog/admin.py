from django.contrib import admin
from .models import Blog, Author


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_authors', 'created_at')
    list_filter = ('created_at',)

    def display_authors(self, obj):
        return ", ".join(author.name for author in obj.author.all())

    display_authors.short_description = 'Authors'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'gender', 'location', 'email', 'date_joined')
    list_filter = ('date_joined',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
