# Generated by Django 3.2.25 on 2024-09-12 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240911_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredient',
            new_name='ingredients',
        ),
    ]
