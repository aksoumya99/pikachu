# Generated by Django 4.1.7 on 2023-03-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_task_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('success', 'success'), ('failure', 'failure'), ('in_progress', 'in_progress')], default='in_progress', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_estimated',
            field=models.IntegerField(null=True),
        ),
    ]
