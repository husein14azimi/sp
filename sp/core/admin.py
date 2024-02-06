from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# admin.site.register(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('first_name',
                           'last_name',
                           "username",
                           'password1',
                           'password2',
                           'phone_number',
                           'email',
                           'profile_image')
            },
        ),
    )


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'thumbnail_tag', 'first_name', 'last_name',
#                     'username', 'owner', 'email', 'cell_phone_1', 'created_jalali', 'updated_jalali')
#     list_filter = ('created', 'updated', 'owner')
#     search_fields = ('first_name', 'last_name', 'username', 'description')

#     list_max_show_all = 10
#     list_per_page = 7
