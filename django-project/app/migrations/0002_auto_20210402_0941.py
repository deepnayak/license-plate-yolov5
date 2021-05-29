# Generated by Django 3.1.7 on 2021-04-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='video',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AddField(
            model_name='profile',
            name='long',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=8),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.CharField(default=None, max_length=100),
        ),
    ]