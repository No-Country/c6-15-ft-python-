# Generated by Django 4.0.4 on 2022-08-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
