from django.contrib import admin

from to_do_list_app.models import Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'date_of_completion']
    list_filter = ['description', 'status', 'date_of_completion']


admin.site.register(Todo, TodoAdmin)
