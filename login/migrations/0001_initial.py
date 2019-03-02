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
