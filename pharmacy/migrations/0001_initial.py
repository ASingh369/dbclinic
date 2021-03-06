# Generated by Django 2.1.4 on 2018-12-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medName', models.CharField(max_length=100)),
                ('medInfo', models.TextField(blank=True)),
                ('medType', models.CharField(max_length=200)),
                ('medImage', models.TextField(blank=True)),
                ('medCost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('medQuantity', models.IntegerField(default=0)),
            ],
        ),
    ]
