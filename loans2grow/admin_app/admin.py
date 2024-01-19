from django.contrib import admin
from .models import User, Family, Bank
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, BaseUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role', 'gender', 'dob', 'signature', 'is_active', 'is_staff','mobile', 'is_superuser', 'permanent_address', 'current_address')}),
        ('Permissions', {'fields': ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


    


    

