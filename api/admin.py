from django.contrib import admin
from .models import StudensModel

# Register your models here.
@admin.register(StudensModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
