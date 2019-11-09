# Generated by Django 2.2.7 on 2019-11-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_id', models.IntegerField()),
                ('mess_name', models.CharField(max_length=50, verbose_name='Mess Name')),
                ('phone', models.CharField(max_length=15, verbose_name='Mess Contact')),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
