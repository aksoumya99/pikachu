# Generated by Django 4.1.7 on 2023-03-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_alter_task_assigned_to_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.CharField(max_length=100, null=True),
        ),
    ]