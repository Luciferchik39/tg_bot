# Generated by Django 5.1.2 on 2025-01-05 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_work_stats_user_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_stats',
            name='user_pk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.botuser'),
        ),
    ]
