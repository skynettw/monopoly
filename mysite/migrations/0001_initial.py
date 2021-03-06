# Generated by Django 4.0.2 on 2022-02-09 00:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('game_id', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('bank', models.PositiveBigIntegerField(default=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('money', models.PositiveBigIntegerField(default=5000)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.game')),
            ],
        ),
    ]
