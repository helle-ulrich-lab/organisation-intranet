# Generated by Django 2.1.8 on 2019-10-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0060_formzbaseelement_donor_organism_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='common_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='common name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='latin_name',
            field=models.CharField(blank=True, help_text='Use FULL latin name, e.g. Homo sapiens', max_length=255, verbose_name='latin name'),
        ),
    ]
