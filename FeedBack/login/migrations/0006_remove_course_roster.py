# Generated by Django 2.1.7 on 2019-04-02 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_course_roster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='roster',
        ),
    ]