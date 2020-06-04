# Generated by Django 3.0.4 on 2020-06-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_award'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='awards',
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.ManyToManyField(to='movies.Award'),
        ),
    ]
