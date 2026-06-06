from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist.'

    def handle(self, *args, **options):
        User = get_user_model()

        email = 'admin@example.com'
        password = 'admin123'

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                username='admin',
                password=password,
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser created: {email} / {password}'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))