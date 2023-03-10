# Generated by Django 4.1.7 on 2023-02-26 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_faculty_positionemployeefaculty_facultymember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Kafedra nomi')),
            ],
            options={
                'verbose_name': 'Kafedra',
                'verbose_name_plural': '3. Kafedralar',
            },
        ),
        migrations.CreateModel(
            name='CafedraEmployeePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Lavozim nomi')),
                ('short_name', models.CharField(max_length=100, unique=True, verbose_name='Lavozimning qisqa nomi')),
            ],
            options={
                'verbose_name': 'Kafedra lavozimi',
                'verbose_name_plural': 'Kafedra lavozimlari',
            },
        ),
        migrations.AlterField(
            model_name='positionemployeefaculty',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Lavozim'),
        ),
        migrations.CreateModel(
            name='CafedraMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon raqami')),
                ('description', models.TextField(blank=True, null=True)),
                ('cafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.cafedra', verbose_name='Kafedra nomi')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.cafedraemployeeposition', verbose_name='Lavozimi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Kafedra hodimi',
                'verbose_name_plural': '5. Fafedra hodimlari',
            },
        ),
    ]
