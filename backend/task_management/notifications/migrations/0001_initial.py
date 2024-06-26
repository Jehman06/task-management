# Generated by Django 5.0.6 on 2024-05-08 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('invitation', 'Invitation to Workspace')], max_length=50)),
                ('content', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('invitation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspaces.invitation')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_received', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications_sent', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspaces.workspace')),
            ],
        ),
    ]
