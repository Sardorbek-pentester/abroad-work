from django.contrib import admin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


class AllUsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('role', 'date_joined')
    inlines = [ProfileInline]
    readonly_fields = ('date_joined',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_role', 'cv_file')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__role',)
    readonly_fields = ('user',)
    
    def user_role(self, obj):
        return obj.user.role
    user_role.short_description = 'Rol'


admin.site.register(User, AllUsersAdmin)
admin.site.register(Profile, ProfileAdmin)