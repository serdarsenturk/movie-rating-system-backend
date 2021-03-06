# Generated by Django 3.0.4 on 2020-06-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200602_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
    ]
