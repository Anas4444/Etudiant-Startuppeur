# Generated by Django 3.2.9 on 2022-04-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_participant_startupidea'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='faculte',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]