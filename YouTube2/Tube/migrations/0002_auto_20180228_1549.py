# Generated by Django 2.0.2 on 2018-02-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='number_subs',
        ),
        migrations.AddField(
            model_name='channel',
            name='number_subscribers',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
    ]