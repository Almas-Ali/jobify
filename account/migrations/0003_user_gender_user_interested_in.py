# Generated by Django 4.2.5 on 2023-10-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='interested_in',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Freelance', 'Freelance'), ('Internship', 'Internship')], default='Full Time', max_length=10),
        ),
    ]
