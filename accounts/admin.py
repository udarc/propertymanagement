from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

    def get_inline_instance(self,request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin,self).get_inline_instance(request,obj)

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)


# def save_model(self, request, obj, form, change):
# super(UserProfileAdmin, self).save_model(request, obj, form, change)
# if not change:
# UserProfile.objects.create(user=obj)