# Generated by Django 2.1.7 on 2019-03-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0004_auto_20190226_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pat_gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
