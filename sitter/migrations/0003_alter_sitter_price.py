# Generated by Django 4.0.4 on 2022-08-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0002_alter_sitter_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='price',
            field=models.PositiveIntegerField(verbose_name='precio'),
        ),
    ]
