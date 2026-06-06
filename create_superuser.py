import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abroad_work.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = os.getenv('SUPER_USERNAME', 'admin')
password = os.getenv('SUPER_PASSWORD', 'admin123')
email = os.getenv('SUPER_EMAIL', 'admin@gmail.com')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("Superuser yaratildi!")
else:
    print("Superuser allaqachon bor!")