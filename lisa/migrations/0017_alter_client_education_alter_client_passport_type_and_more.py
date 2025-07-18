# Generated by Django 5.2.4 on 2025-07-17 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisa', '0016_alter_client_education_alter_client_passport_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='education',
            field=models.CharField(choices=[('1', 'Oliy'), ('3', 'O‘rta-maxsus'), ('4', 'Tuganlanmagan oliy'), ('2', 'O‘rta'), ('5', 'Boshlang‘ich')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport_type',
            field=models.CharField(blank=True, choices=[('old_pass', 'Eski turdagi passport'), ('drivers_license', 'Haydovchilik guvohnomasi'), ('id', 'ID passport')], default='id', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='credit',
            name='status',
            field=models.CharField(choices=[('rejected', 'rad etildi'), ('pending', 'jarayonda'), ('done', 'berildi')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
