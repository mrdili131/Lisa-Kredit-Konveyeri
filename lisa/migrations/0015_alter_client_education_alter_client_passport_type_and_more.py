# Generated by Django 5.2.4 on 2025-07-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisa', '0014_alter_client_education_alter_client_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='education',
            field=models.CharField(choices=[('5', 'Boshlang‘ich'), ('4', 'Tuganlanmagan oliy'), ('2', 'O‘rta'), ('3', 'O‘rta-maxsus'), ('1', 'Oliy')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport_type',
            field=models.CharField(blank=True, choices=[('id', 'ID passport'), ('drivers_license', 'Haydovchilik guvohnomasi'), ('old_pass', 'Eski turdagi passport')], default='id', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='credit',
            name='status',
            field=models.CharField(choices=[('pending', 'jarayonda'), ('rejected', 'rad etildi'), ('done', 'berildi')], default='pending', max_length=50),
        ),
    ]
