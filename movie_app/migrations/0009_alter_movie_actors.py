# Generated by Django 4.2 on 2023-04-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_alter_movie_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='movie_app.actor'),
        ),
    ]
