# Generated by Django 3.0.1 on 2021-03-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_cancelledapproval_refund_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_type', models.CharField(max_length=50)),
                ('email_subject', models.CharField(max_length=50)),
                ('email_body', models.CharField(max_length=50)),
                ('email_sender', models.CharField(max_length=50)),
                ('email_recipients', models.CharField(max_length=50)),
            ],
        ),
    ]