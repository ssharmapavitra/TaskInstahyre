# Generated by Django 4.2.8 on 2023-12-20 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_remove_userprofile_user_delete_spamreport_and_more'),
        ('spam', '0003_alter_spamreport_reporter_delete_contact_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
