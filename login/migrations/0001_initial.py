<<<<<<< HEAD
# Generated by Django 2.1.7 on 2019-03-01 13:45
=======
# Generated by Django 2.1.7 on 2019-03-02 03:36
>>>>>>> 69fd464fa73e484afe50f06b83774eade789b9bf

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginId', models.CharField(max_length=100)),
                ('passWord', models.CharField(max_length=100)),
                ('userType', models.CharField(max_length=30)),
            ],
        ),
    ]