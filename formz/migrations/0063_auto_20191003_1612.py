# Generated by Django 2.1.8 on 2019-10-03 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0062_remove_formzbaseelement_donor_organism'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formzbaseelement',
            old_name='donor_organism_species',
            new_name='donor_organism',
        ),
    ]
