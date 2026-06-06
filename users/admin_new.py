from django.contrib import admin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


class EmployerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('date_joined',)
    inlines = [ProfileInline]
    readonly_fields = ('role',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role='employer')


class JobSeekerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('date_joined',)
    inlines = [ProfileInline]
    readonly_fields = ('role',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role='job_seeker')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_role', 'cv_file')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__role',)
    readonly_fields = ('user',)
    
    def user_role(self, obj):
        return obj.user.role
    user_role.short_description = 'Role'


admin.site.register(User, EmployerUserAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.site_header = "Work Abroad Admin"
admin.site.site_title = "Work Abroad"
