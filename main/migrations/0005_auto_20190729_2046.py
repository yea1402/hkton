# Generated by Django 2.2.3 on 2019-07-29 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190729_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='djangoboard',
            old_name='lisence',
            new_name='license',
        ),
    ]
