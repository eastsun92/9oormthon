# Generated by Django 4.2.7 on 2023-12-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goormthon_app', '0008_alter_jejutouristspot_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jejutouristspot',
            name='url',
            field=models.CharField(max_length=15000, null=True),
        ),
    ]