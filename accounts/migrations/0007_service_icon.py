# Generated by Django 5.1.7 on 2025-03-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
