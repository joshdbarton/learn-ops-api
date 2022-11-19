# Generated by Django 4.0.3 on 2022-10-26 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0008_dailystatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learningrecordentry',
            options={'ordering': ('-recorded_on',)},
        ),
        migrations.AddField(
            model_name='capstone',
            name='repo_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='StudentPersonality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('briggs_myers_type', models.CharField(blank=True, max_length=6, null=True)),
                ('bfi_extraversion', models.IntegerField()),
                ('bfi_agreeableness', models.IntegerField()),
                ('bfi_conscientiousness', models.IntegerField()),
                ('bfi_neuroticism', models.IntegerField()),
                ('bfi_openness', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personality', to='LearningAPI.nssuser')),
            ],
        ),
    ]