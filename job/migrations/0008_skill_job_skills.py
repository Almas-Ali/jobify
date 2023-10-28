# Generated by Django 4.2.5 on 2023-10-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_application_cover_letter_application_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='job_skills', to='job.skill'),
        ),
    ]