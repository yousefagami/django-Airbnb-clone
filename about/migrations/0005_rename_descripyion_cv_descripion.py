# Generated by Django 4.0.4 on 2022-05-10 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_cv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='descripyion',
            new_name='descripion',
        ),
    ]
