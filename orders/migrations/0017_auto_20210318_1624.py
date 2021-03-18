# Generated by Django 3.0.1 on 2021-03-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20210318_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelledorder',
            name='final_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='cancelledorder',
            name='gst_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]