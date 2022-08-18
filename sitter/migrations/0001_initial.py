# Generated by Django 4.0.4 on 2022-08-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('picture_site', models.ImageField(upload_to='sitter/img/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
    ]
