from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


class EmployerAdmin(BaseUserAdmin):
    """Ish beruvchilarni ko'rsatadi"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [ProfileInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(role='employer')


class JobSeekerAdmin(BaseUserAdmin):
    """Ish izlovchilarni ko'rsatadi"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [ProfileInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(role='job_seeker')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_role', 'cv_file')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__role',)
    readonly_fields = ('user',)
    
    def user_role(self, obj):
        return obj.user.role
    user_role.short_description = 'Rol'


# Ish beruvchilar
admin.site.register(User, EmployerAdmin)

# Profil
admin.site.register(Profile, ProfileAdmin)

# Admin nomlanishi
admin.site.site_header = "Work Abroad Admin"
admin.site.site_title = "Work Abroad"
