from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Posts, Profile

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username", "email", "password"]
    inlines = [ProfileInline]  # Make profile inline with user. No separate places

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Profile)

admin.site.register(Posts)

