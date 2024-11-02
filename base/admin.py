from django.contrib import admin

# Register your models here.
from .models import Room, Course_Teacher, Team_member_Info, Topic, Message

admin.site.register(Room) #to show/resiger the Room model/table in the admin panel
admin.site.register(Course_Teacher)
admin.site.register(Team_member_Info)
admin.site.register(Topic)
admin.site.register(Message)