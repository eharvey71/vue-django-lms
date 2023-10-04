from django.contrib import admin

from .models import Category, Course, Lesson, Comment, Quiz

class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['lesson']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'status', 'lesson_type']
    list_filter = ['status','lesson_type']
    search_fields = ['title', 'short_description', 'long_description']
    inlines = [LessonCommentInline]

admin.site.site_title = "MicroMastery Administration"
admin.site.index_title = "Welcome to the MicroMastery Admin Portal"
admin.site.site_header = "MicroMastery Administration"

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)
admin.site.register(Quiz)