import os
import sys
from pathlib import Path
import django

# Ensure project root is on sys.path so Django can import the project package
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abroad_work.settings')
django.setup()

from users.models import User


def create_user(email, username, role, password):
    user, created = User.objects.get_or_create(email=email, defaults={'username': username, 'role': role})
    user.username = username
    user.role = role
    user.set_password(password)
    user.save()
    return created


if __name__ == '__main__':
    accounts = [
        ('employer@example.com', 'employeruser', User.EMPLOYER, 'EmployerPass123!'),
        ('seeker@example.com', 'seekeruser', User.JOB_SEEKER, 'SeekerPass123!'),
    ]

    for email, username, role, password in accounts:
        created = create_user(email, username, role, password)
        status = 'created' if created else 'updated'
        print(f'{email} ({role}) -> {status}')

    print('Done.')
