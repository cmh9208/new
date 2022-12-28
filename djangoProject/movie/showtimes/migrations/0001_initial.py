# Generated by Django 4.1.4 on 2022-12-27 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0001_initial'),
        ('movies', '0001_initial'),
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieShowtime',
            fields=[
                ('showtime_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('movie_cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.moviecinema')),
                ('movie_movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('movie_theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theaters.movietheater')),
            ],
            options={
                'db_table': 'movie_showtimes',
            },
        ),
    ]