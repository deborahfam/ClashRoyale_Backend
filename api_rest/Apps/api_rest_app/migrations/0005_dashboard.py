# Generated by Django 4.0.5 on 2022-06-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest_app', '0004_delete_oauth_remove_roles_scopes_r_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]