# Generated by Django 2.2.8 on 2020-02-29 01:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0020_auto_20200218_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bitbyteactivity',
            old_name='confirm_date',
            new_name='request_date',
        ),
        migrations.RemoveField(
            model_name='bitbyteactivity',
            name='candidate',
        ),
        migrations.AddField(
            model_name='bitbyteactivity',
            name='candidates',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitbyteactivity',
            name='confirmed',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='bitbyteactivity',
            name='proof',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
    ]
