# Generated by Django 2.1.7 on 2019-04-09 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_homework'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='cour1se',
            new_name='course',
        ),
    ]
