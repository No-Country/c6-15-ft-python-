# Generated by Django 4.0.4 on 2022-08-16 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='descripcion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
