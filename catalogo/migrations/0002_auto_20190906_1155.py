# Generated by Django 2.2.5 on 2019-09-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajos',
            name='website',
        ),
        migrations.AddField(
            model_name='autor',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='fecha_publicado',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='picture',
            field=models.FileField(blank=True, upload_to='pictures'),
        ),
    ]
