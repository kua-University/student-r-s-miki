# Generated by Django 5.1.2 on 2025-01-02 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('students', '0003_alter_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='students', to='auth.group'),
        ),
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='students', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]