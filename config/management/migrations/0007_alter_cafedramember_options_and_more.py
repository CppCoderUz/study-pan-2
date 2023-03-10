# Generated by Django 4.1.7 on 2023-02-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_cafedra_cafedraemployeeposition_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cafedramember',
            options={'verbose_name': 'Kafedra hodimi', 'verbose_name_plural': '5. Kafedra hodimlari'},
        ),
        migrations.AlterField(
            model_name='cafedraemployeeposition',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Lavozimning qisqa nomi'),
        ),
    ]
