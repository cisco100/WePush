from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from certify.models import Account
from certify.forms import UserCreationForm, UserChangeForm


class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
#'email', 'name', 'phone', 'date_of_birth', 'picture', 'password','education_level','field_of_interest','update_me_on_my_field'
    list_display = ('email', 'name', 'phone', 'date_of_birth', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'date_of_birth','gender', 'picture')}),
        ('Educational Info', {'fields': ('education_level', 'field_of_interest', 'update_me_on_my_field')}),
        #('Educational Info',{'fields':('education_level','field_of_interest','update_me_on_my_field')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth','gender', 'picture')}),
        ('Educational info', {'fields': ('education_level', 'field_of_interest', 'update_me_on_my_field')}),

       # ('Educational Info',{'fields':('education_level','field_of_interest','update_me_on_my_field')})
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
