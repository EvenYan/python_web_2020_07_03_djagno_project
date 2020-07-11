from django.contrib import admin
from my_app.models import *

# Register your models here.


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'math', 'chinese')
    search_fields = ("name", 'math')
    list_filter = ("name", 'math')
    list_per_page = 5
    ordering = ['math']
    # fields = ('name', 'math')
    fieldsets = (("基本信息", {"fields": ('name', )}), ("详细信息", {"fields":("math","chinese")}))


class StudentInline(admin.StackedInline):
    model = Student
    extra = 3


def gender(self):
    if self.gender:
        return "男"
    return "女"

gender.short_description = "性别"


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", gender)


class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(Post)
admin.site.register(Score, ScoreAdmin)
admin.site.register(UserInfo)
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(People)
admin.site.register(IDCard)
admin.site.register(Category)
admin.site.register(Tag)