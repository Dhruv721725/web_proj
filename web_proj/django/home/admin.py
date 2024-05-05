from django.contrib import admin
from home.models import *
# Register your models here.
admin.site.register(Recipies)
admin.site.register(StudentId)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Sub)

class SubMarksAdmin(admin.ModelAdmin):
    list_display=['st_name','sub_name','marks']
admin.site.register(Sub_marks,SubMarksAdmin)
