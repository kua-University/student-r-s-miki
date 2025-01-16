# Generated by Django 5.1.2 on 2025-01-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_groups_student_is_active_student_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=22),
        ),
    ]