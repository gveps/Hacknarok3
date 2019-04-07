from django.contrib import admin

from api.models import Task, Tag, TagTask, TaskUser, MyUser, Challange, TaskChallange, CategoryTag

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(TagTask)
admin.site.register(TaskUser)
admin.site.register(MyUser)
admin.site.register(Challange)
admin.site.register(TaskChallange)
admin.site.register(CategoryTag)
