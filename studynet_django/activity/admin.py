from django.contrib import admin

from .models import Activity

class ActivityInline(admin.TabularInline):
    model = Activity
#    raw_id_fields = ['lesson']

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'status', 'created_by']
    list_filter = ['status','created_by']

#admin.site.register(Activity, ActivityAdmin)
admin.site.register(Activity, ActivityAdmin)