# Generated by Django 4.0.4 on 2022-08-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_rename_petowner_id_pet_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='accesories',
            field=models.CharField(max_length=255, verbose_name='accesorios de la mascota'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(verbose_name='edad de mascota'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='condition',
            field=models.CharField(max_length=255, verbose_name='Condiciones de la mascota'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=20, verbose_name='nombre de la mascota'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(max_length=255, verbose_name='talla de la mascota'),
        ),
    ]