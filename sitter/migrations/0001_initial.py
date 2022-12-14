# Generated by Django 4.0.4 on 2022-08-26 15:21

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
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='precio')),
                ('descripcion', models.CharField(max_length=255, verbose_name='descripcion')),
                ('status', models.IntegerField(choices=[(1, 'Activa'), (2, 'Inactiva')], default=1, verbose_name='activo')),
                ('picture_site', models.ImageField(blank=True, null=True, upload_to='sitters/', verbose_name='foto del sitio')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
