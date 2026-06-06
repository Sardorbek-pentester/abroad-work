from django.contrib import admin
from .models import Job, ConsultationRequest, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'country', 'approved', 'featured', 'created_at')
    list_filter = ('country', 'featured', 'approved', 'created_at')
    search_fields = ('title', 'company', 'description')
    readonly_fields = ('created_at',)
    actions = ['approve_jobs', 'unapprove_jobs']
    
    def approve_jobs(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} ta ish tasdiqlandi.')
    approve_jobs.short_description = "Tanlangan ishlarni tasdiqlash"
    
    def unapprove_jobs(self, request, queryset):
        updated = queryset.update(approved=False)
        self.message_user(request, f'{updated} ta ish rad etildi.')
    unapprove_jobs.short_description = "Tanlangan ishlarni rad etish"
    
    def save_model(self, request, obj, form, change):
        if not obj.posted_by:
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email', 'user__username', 'job__title')
    readonly_fields = ('created_at',)


class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'interested_country', 'profession', 'created_at')
    list_filter = ('interested_country', 'created_at')
    search_fields = ('full_name', 'email', 'profession')
    readonly_fields = ('created_at',)


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ConsultationRequest, ConsultationRequestAdmin)
