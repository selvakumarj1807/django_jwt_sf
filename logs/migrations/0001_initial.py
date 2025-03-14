# Generated by Django 5.1.7 on 2025-03-13 08:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('received_timestamp', models.DateTimeField(auto_now_add=True)),
                ('processed_timestamp', models.DateTimeField(blank=True, null=True)),
                ('received_data', models.JSONField()),
                ('status', models.CharField(choices=[('success', 'Success'), ('failed', 'Failed')], max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.destination')),
            ],
        ),
    ]
