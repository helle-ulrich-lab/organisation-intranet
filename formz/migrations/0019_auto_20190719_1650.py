# Generated by Django 2.1.8 on 2019-07-19 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0018_storagelocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagelocation',
            name='collection_models',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType', verbose_name='collection models'),
        ),
    ]