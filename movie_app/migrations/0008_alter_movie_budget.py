# Generated by Django 4.2 on 2023-04-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_actor_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
