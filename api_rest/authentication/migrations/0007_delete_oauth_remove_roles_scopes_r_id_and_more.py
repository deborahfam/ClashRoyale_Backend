# Generated by Django 4.0.5 on 2022-06-18 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OAuth',
        ),
        migrations.RemoveField(
            model_name='roles_scopes',
            name='R_ID',
        ),
        migrations.RemoveField(
            model_name='roles_scopes',
            name='SC_ID',
        ),
        migrations.RemoveField(
            model_name='user_scopes',
            name='SC_ID',
        ),
        migrations.RemoveField(
            model_name='user_scopes',
            name='U_ID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='Roles_Scopes',
        ),
        migrations.DeleteModel(
            name='Scopes',
        ),
        migrations.DeleteModel(
            name='User_Scopes',
        ),
    ]
