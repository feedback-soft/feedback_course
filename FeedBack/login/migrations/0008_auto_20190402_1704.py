# Generated by Django 2.1.7 on 2019-04-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_user_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_intorduction',
            new_name='course_introduction',
        ),
    ]