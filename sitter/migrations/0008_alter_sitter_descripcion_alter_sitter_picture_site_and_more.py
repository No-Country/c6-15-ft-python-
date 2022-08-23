# Generated by Django 4.0.4 on 2022-08-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0007_alter_sitter_picture_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='descripcion',
            field=models.CharField(max_length=255, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='picture_site',
            field=models.ImageField(blank=True, null=True, upload_to='sitters/', verbose_name='foto del sitio'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='price',
            field=models.PositiveIntegerField(verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='status',
            field=models.IntegerField(choices=[(1, 'Activa'), (2, 'Inactiva')], default=1, verbose_name='activo'),
        ),
    ]