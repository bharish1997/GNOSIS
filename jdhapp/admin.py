from django.contrib import admin
from .models import Category,Course,Instructor,Student
admin.site.site_header = "GNOSIS"
admin.site.index_title = " "

admin.site.register(Instructor)
admin.site.register(Student)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass