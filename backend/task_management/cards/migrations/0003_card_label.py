# Generated by Django 5.0.6 on 2024-05-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='label',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]
