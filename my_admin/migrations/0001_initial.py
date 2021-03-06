# Generated by Django 2.1.13 on 2019-11-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_admin_email_address', models.EmailField(max_length=254, verbose_name="site admin's email address")),
                ('order_email_addresses', models.EmailField(help_text='Email address to send urgent order notifications', max_length=254, verbose_name='order email address')),
                ('saveris_username', models.CharField(max_length=255, verbose_name='saveris username')),
                ('saveris_password', models.CharField(max_length=255, verbose_name='saveris password')),
                ('join_api_key', models.CharField(max_length=255, verbose_name='join api key')),
            ],
            options={
                'verbose_name': 'general setting',
                'verbose_name_plural': 'general settings',
            },
        ),
    ]
