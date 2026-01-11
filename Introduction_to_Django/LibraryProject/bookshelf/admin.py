from django.contrib import admin

# Register your models here.

from .models import Book

admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    list_filter = ('publication_year', 'author')            # sidebar filters
    search_fields = ('title', 'author')                     # search box

admin.site.register(Book, BookAdmin)
