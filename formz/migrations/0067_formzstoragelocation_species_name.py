# Generated by Django 2.1.8 on 2019-10-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0066_remove_formzstoragelocation_species_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='formzstoragelocation',
            name='species_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='formz.Species', verbose_name='species name'),
        ),
    ]
