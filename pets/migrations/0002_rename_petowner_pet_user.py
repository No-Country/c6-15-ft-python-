# Generated by Django 4.0.4 on 2022-08-12 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='petowner',
            new_name='user',
        ),
    ]
