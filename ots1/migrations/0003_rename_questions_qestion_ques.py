# Generated by Django 4.2.2 on 2023-07-21 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ots1', '0002_alter_candidate_points_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qestion',
            old_name='questions',
            new_name='ques',
        ),
    ]
