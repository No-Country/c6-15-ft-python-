# Generated by Django 4.0.4 on 2022-08-21 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='nombre de la mascota')),
                ('age', models.IntegerField(verbose_name='edad de mascota')),
                ('size', models.CharField(max_length=255, verbose_name='talla de la mascota')),
                ('condition', models.CharField(max_length=255, verbose_name='Condiciones de la mascota')),
                ('accesories', models.CharField(max_length=255, verbose_name='accesorios de la mascota')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
