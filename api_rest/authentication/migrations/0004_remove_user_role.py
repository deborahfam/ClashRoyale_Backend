# Generated by Django 4.0.5 on 2022-06-11 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_u_role_user_role_remove_user_u_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]