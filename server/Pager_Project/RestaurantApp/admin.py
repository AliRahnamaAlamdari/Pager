from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

admin.site.register(AppUser)
# class UserAdmin(DefaultUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {
#             'fields': (
#                 'first_name',
#                 'last_name',
#                 'username',
#                 'email',
#                 'phone_number',
#                 'province',
#                 'city',
#                 'adress',
#                 'signing_date',
#                 'role'

#             )
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active',
#                 'is_staff',
#                 'is_superuser',
#                 'groups',
#                 'user_permissions'
#             ),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

#     list_display = (
#         'username',
#         'email',
#         'phone_number',
#         'province',
#         'city',
#         'adress',
#         'signing_date',
#         'role',
#         'is_staff'
#     )

#     search_fields = (
#         'username',
#         'email',
#         'phone_number',
#         'province',
#         'city',
#         'adress',
#         'signing_date',
#         'role',
#     )
admin.site.register(FoodGroup)
admin.site.register(FoodItem)
admin.site.register(Restaurant)
