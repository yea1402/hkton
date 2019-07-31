# Generated by Django 2.2.3 on 2019-07-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='djangoboard',
            old_name='memo',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='djangoboard',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='djangoboard',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='djangoboard',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='djangoboard',
            name='subject',
        ),
        migrations.AddField(
            model_name='djangoboard',
            name='body',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='djangoboard',
            name='lisence',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]