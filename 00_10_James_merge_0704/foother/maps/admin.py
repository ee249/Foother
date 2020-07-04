from import_export import resources
from django.contrib import admin
from .models import Review
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource

admin.site.register(Review, ReviewAdmin)