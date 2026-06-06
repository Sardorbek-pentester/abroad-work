from jobs.models import Job
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.filter(role='employer').first()
if user:
    print(f"Found user: {user}")
    job = Job.objects.create(title='Test', country='Test', city='Test', salary='Test', experience='Test', description='Test', company='Test Company', posted_by=user)
    print(f"Job created successfully: {job}")
else:
    print("No employer user found")