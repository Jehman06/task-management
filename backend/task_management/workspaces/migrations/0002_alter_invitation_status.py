# Generated by Django 5.0.6 on 2024-05-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('pending', 'Pending'), ('accepted', 'Accepted')], max_length=20),
        ),
    ]
