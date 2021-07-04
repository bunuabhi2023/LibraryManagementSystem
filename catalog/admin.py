from django.contrib import admin

# Register your models here.
from .models import Book,BookInstance,Author
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author' )
#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

fieldsets = (
    (None, {
        'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back')
    }),
)
#admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

