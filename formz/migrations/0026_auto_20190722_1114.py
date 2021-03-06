# Generated by Django 2.1.8 on 2019-07-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formz', '0025_auto_20190722_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formzproject',
            name='beginning_work_date',
            field=models.DateField(help_text='<i>Beginn der Arbeiten</i>', null=True, verbose_name='beginning of work'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='donor_organims',
            field=models.CharField(blank=True, help_text='Used organisms, their risk group and safety-relevant properties. <i>Verwendete Spenderorganismen</i>', max_length=255, verbose_name='donor organisms'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='generated_gmo',
            field=models.TextField(blank=True, help_text='Include risk groups and safety-relevant properties. <i>Erzeugte GVO</i>', verbose_name='generated GMOs'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='hazard_activity',
            field=models.TextField(blank=True, help_text='<i>Gefährdungsrelevante Merkmale der Tätigkeit</i>', verbose_name='hazard-relevant characteristics of activity'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='hazards_employee',
            field=models.TextField(blank=True, help_text='<i>Schwere und Wahrscheinlichkeit einer Gefährdung der Mitarbeiter und/oder der Umwelt</i>', verbose_name='severity and likelihood of hazards to employees and/or the environment'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='objectives',
            field=models.CharField(blank=True, help_text='<i>Zielsetzung</i>', max_length=255, verbose_name='objectives of strategy'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='potential_risk_nuc_acid',
            field=models.TextField(blank=True, help_text='Include safety-relevant properties. <i>Gefährdungspotentiale der übertragenen Nukleinsäuren</i>', verbose_name='potential risks of transferred nucleic acids'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='project_leader',
            field=models.CharField(help_text='<i>Projektleiter</i>', max_length=255, verbose_name='project leader'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='recipient_organisms',
            field=models.CharField(blank=True, help_text='Include risk groups and safety-relevant properties. <i>Verwendete Empfängerorganismen</i>', max_length=255, verbose_name='recipient organisms'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='safety_level',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2)], help_text='<i>Sicherheitsstufe</i>', null=True, verbose_name='safety level'),
        ),
        migrations.AlterField(
            model_name='formzproject',
            name='title',
            field=models.CharField(help_text='<i>titel</i>', max_length=191, verbose_name='title'),
        ),
    ]
