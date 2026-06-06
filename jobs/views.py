from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application, ConsultationRequest
from .forms import ConsultationForm
from blog.models import BlogPost

def home(request):

    featured_jobs = Job.objects.filter(featured=True, approved=True).order_by('-created_at')[:6]

    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'featured_jobs': featured_jobs,
        'latest_posts': latest_posts,
    })
@login_required
def jobs_list(request):
    jobs = Job.objects.filter(approved=True).order_by('-created_at')

    title = request.GET.get('title')
    country = request.GET.get('country')
    city = request.GET.get('city')
    company = request.GET.get('company')
    experience = request.GET.get('experience')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    if title:
        jobs = jobs.filter(title__icontains=title)

    if country:
        jobs = jobs.filter(country__icontains=country)

    if city:
        jobs = jobs.filter(city__icontains=city)

    if company:
        jobs = jobs.filter(company__icontains=company)

    if experience:
        jobs = jobs.filter(experience__icontains=experience)

    if min_salary:
        jobs = jobs.filter(salary__gte=min_salary)

    if max_salary:
        jobs = jobs.filter(salary__lte=max_salary)

    countries = Job.objects.values_list('country', flat=True).distinct()
    cities = Job.objects.values_list('city', flat=True).distinct()
    companies = Job.objects.values_list('company', flat=True).distinct()
    experiences = Job.objects.values_list('experience', flat=True).distinct()

    return render(request, 'jobs.html', {
        'jobs': jobs,
        'countries': countries,
        'cities': cities,
        'companies': companies,
        'experiences': experiences,
    })
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    # Allow access if: approved OR user is the poster OR user is admin
    if not job.approved and (not request.user.is_authenticated or (job.posted_by != request.user and not request.user.is_staff)):
        return render(request, '404.html', status=404)
    return render(request, 'job_detail.html', {'job': job})


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    # Check if job is approved
    if not job.approved:
        messages.error(request, "Bu ish hali tasdiqlanmagan.")
        return redirect('jobs_list')

    already_applied = Application.objects.filter(user=request.user, job=job).exists()
    if not already_applied:
        Application.objects.create(user=request.user, job=job)

    return redirect('profile')

@login_required
def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojaatingiz qabul qilindi. Tez orada siz bilan bog'lanamiz.")
            return redirect('home')
    else:
        form = ConsultationForm()

    return render(request, 'consultation.html', {'form': form})