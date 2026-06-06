
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import RegisterForm, ProfileForm, LoginForm
from .models import Profile
from jobs.models import Application, Job
from .decorators import employer_required, job_seeker_required

# Registration view (already role-aware)
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            login(request, user)
            if user.role == 'employer':
                return redirect('employer_dashboard')
            elif user.role == 'job_seeker':
                return redirect('job_seeker_dashboard')
            else:
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view with role-based redirect
def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts=None):
                return redirect(next_url)
            return redirect_by_role(user)
        else:
            messages.error(request, "Email yoki parol noto'g'ri.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil yangilandi.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    applications = Application.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {
        'profile': profile,
        'form': form,
        'applications': applications,
    })

# Role-based redirect helper
def redirect_by_role(user):
    if user.role == 'employer':
        return redirect('employer_dashboard')
    elif user.role == 'job_seeker':
        return redirect('home')
    else:
        return redirect('home')

# Employer dashboard and features
@login_required
@employer_required
def employer_dashboard(request):
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'employer/dashboard.html', {'jobs': jobs})

@login_required
@employer_required
def employer_create_job(request):
    from jobs.forms import JobForm
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.username
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Ish qo\'shildi! Admin tasdiqlagandan keyin ko\'rinadi.')
            return redirect('employer_my_jobs')
    else:
        form = JobForm()
    return render(request, 'employer/create_job.html', {'form': form})

@login_required
@employer_required
def employer_my_jobs(request):
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'employer/my_jobs.html', {'jobs': jobs})

@login_required
@employer_required
def employer_view_applications(request, job_id=None):
    if job_id:
        job = get_object_or_404(Job, id=job_id, posted_by=request.user)
        applications = Application.objects.filter(job=job)
        return render(request, 'employer/view_applications.html', {'applications': applications, 'job': job})
    else:
        jobs = Job.objects.filter(posted_by=request.user)
        return render(request, 'employer/my_jobs.html', {'jobs': jobs})

# Job Seeker dashboard and features
@login_required
@job_seeker_required
def job_seeker_dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'seeker/dashboard.html', {'applications': applications})

@login_required
@job_seeker_required
def seeker_browse_jobs(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'seeker/browse_jobs.html', {'jobs': jobs})

@login_required
@job_seeker_required
def seeker_apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    already_applied = Application.objects.filter(user=request.user, job=job).exists()
    if not already_applied:
        Application.objects.create(user=request.user, job=job)
        messages.success(request, 'Applied successfully!')
    return redirect('seeker_view_applications')

@login_required
@job_seeker_required
def seeker_view_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'seeker/view_applications.html', {'applications': applications})