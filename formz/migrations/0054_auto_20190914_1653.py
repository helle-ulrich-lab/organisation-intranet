# Generated by Django 2.1.8 on 2019-09-14 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formz', '0053_auto_20190914_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formzproject',
            name='project_leader',
        ),
        migrations.AddField(
            model_name='formzproject',
            name='project_leader',
            field=models.ManyToManyField(help_text='<i>Projektleiter</i>', null=True, to=settings.AUTH_USER_MODEL, verbose_name='project leaders'),
        ),
    ]
