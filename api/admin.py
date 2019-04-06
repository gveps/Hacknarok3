from django.contrib import admin

from api.models import Task, Tag, TagTask, TaskUser

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(TagTask)
admin.site.register(TaskUser)
