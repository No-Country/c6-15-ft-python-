# Generated by Django 4.0.4 on 2022-08-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.IntegerField(choices=[(1, 'Activa'), (2, 'Inactiva')], default=1),
        ),
    ]
