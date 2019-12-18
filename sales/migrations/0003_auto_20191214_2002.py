# Generated by Django 3.0 on 2019-12-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20191214_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]