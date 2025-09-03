from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # columns shown in list
    search_fields = ("title", "author")                      # search box fields
    list_filter = ("publication_year",)                      # filters on the right


