# Generated by Django 5.1.11 on 2025-07-06 18:50

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=courses.models.handle_upload)),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email required')], default='email_required', max_length=15)),
                ('status', models.CharField(choices=[('publish', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=10)),
            ],
        ),
    ]
