from django.contrib import admin
from .models import Author, Quotations, Quotation
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Author


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quotations)
admin.site.register(Quotation)
