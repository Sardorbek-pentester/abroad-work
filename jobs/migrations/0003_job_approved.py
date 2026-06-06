from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
