# Generated by Django 4.2.7 on 2023-12-06 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goormthon_app', '0004_rename_phonenumber_jejutouristspot_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jejutouristspot',
            old_name='URL',
            new_name='url',
        ),
    ]
