# Generated by Django 4.0.4 on 2022-08-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='petowner_id',
            new_name='user_id',
        ),
    ]
