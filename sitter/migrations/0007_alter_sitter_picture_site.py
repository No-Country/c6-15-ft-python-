# Generated by Django 4.0.4 on 2022-08-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0006_alter_sitter_picture_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='picture_site',
            field=models.ImageField(blank=True, null=True, upload_to='sitters/'),
        ),
    ]
