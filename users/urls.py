from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .views import (
    register_view, login_view, logout_view, profile_view,
    employer_dashboard, employer_create_job, employer_my_jobs, employer_view_applications,
    job_seeker_dashboard, seeker_browse_jobs, seeker_apply_job, seeker_view_applications
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Employer URLs
    path('employer/dashboard/', employer_dashboard, name='employer_dashboard'),
    path('employer/create-job/', employer_create_job, name='employer_create_job'),
    path('employer/my-jobs/', employer_my_jobs, name='employer_my_jobs'),
    path('employer/applications/<int:job_id>/', employer_view_applications, name='employer_view_applications'),

    # Job Seeker URLs
    path('seeker/dashboard/', job_seeker_dashboard, name='job_seeker_dashboard'),
    path('seeker/browse-jobs/', seeker_browse_jobs, name='seeker_browse_jobs'),
    path('seeker/apply/<int:job_id>/', seeker_apply_job, name='seeker_apply_job'),
    path('seeker/applications/', seeker_view_applications, name='seeker_view_applications'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('password_reset_done'),
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete'),
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]