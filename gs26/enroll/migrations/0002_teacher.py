# Generated by Django 3.2.7 on 2021-09-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_roll', models.IntegerField()),
                ('t_name', models.CharField(max_length=50)),
                ('t_dep', models.CharField(max_length=50)),
                ('t_email', models.EmailField(max_length=40)),
            ],
        ),
    ]