# Generated by Django 2.2.5 on 2019-09-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20190912_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['-fecha_agregado'], 'verbose_name_plural': 'Pictures'},
        ),
        migrations.AddField(
            model_name='pictures',
            name='fecha_agregado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
