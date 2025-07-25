# Generated by Django 5.2 on 2025-07-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisa', '0004_credit_filial_alter_client_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='education',
            field=models.CharField(choices=[('2', 'O‘rta'), ('3', 'O‘rta-maxsus'), ('5', 'Boshlang‘ich'), ('4', 'Tuganlanmagan oliy'), ('1', 'Oliy')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('Female', 'Ayol'), ('Male', 'Erkak')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.CharField(choices=[('old_pass', 'Eski turdagi passport'), ('id', 'ID passport'), ('drivers_license', 'Haydovchilik guvohnomasi')], default='id', max_length=50),
        ),
        migrations.AlterField(
            model_name='credit',
            name='status',
            field=models.CharField(choices=[('rejected', 'rad etildi'), ('pending', 'jarayonda'), ('done', 'berildi')], default='pending', max_length=50),
        ),
    ]
