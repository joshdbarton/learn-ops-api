# Generated by Django 4.0.3 on 2023-02-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0029_course_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohortcourse',
            name='index',
            field=models.SmallIntegerField(default=1),
        ),
    ]
