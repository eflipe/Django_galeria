# Generated by Django 2.2.5 on 2019-09-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20190906_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
