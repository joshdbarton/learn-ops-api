# Generated by Django 4.0.3 on 2023-01-19 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0027_alter_project_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_projects', to='LearningAPI.book'),
        ),
    ]
