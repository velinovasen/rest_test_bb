# Generated by Django 3.1 on 2020-08-26 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200826_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='continent',
        ),
    ]
