<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 2.2b1 on 2019-03-02 03:41
=======
<<<<<<< HEAD
# Generated by Django 2.1.7 on 2019-03-01 13:45
=======
# Generated by Django 2.1.7 on 2019-03-02 03:36
>>>>>>> 69fd464fa73e484afe50f06b83774eade789b9bf
>>>>>>> 2942167e63d0559f7c2cefef308111c6be3af7e3
=======
# Generated by Django 2.1.7 on 2019-03-02 03:36
>>>>>>> 986a3903ce1da1afe0601ef6637fd62d065b0ab6

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecepID', models.CharField(max_length=20)),
                ('DocsID', models.CharField(max_length=20)),
                ('HospitalID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 2942167e63d0559f7c2cefef308111c6be3af7e3
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNumber', models.CharField(max_length=20)),
                ('CaseName', models.CharField(max_length=20)),
                ('CaseInfo', models.CharField(max_length=250)),
                ('Medicines', models.CharField(max_length=100)),
                ('DocUploads', models.FileField(upload_to='')),
<<<<<<< HEAD
                ('Docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Docs')),
            ],
        ),
=======
            ],
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecepID', models.CharField(max_length=20)),
                ('DocsID', models.CharField(max_length=20)),
                ('HospitalID', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='Docs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Docs'),
        ),
>>>>>>> 2942167e63d0559f7c2cefef308111c6be3af7e3
    ]
