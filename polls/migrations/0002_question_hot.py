# Generated by Django 2.1 on 2018-08-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hot',
            field=models.IntegerField(default=0),
        ),
    ]
