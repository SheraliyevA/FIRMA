# Generated by Django 5.0.2 on 2024-02-18 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0014_alter_user_status_remove_xodim_ish_turi_bulim_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Missed',
            new_name='Workinspection',
        ),
    ]