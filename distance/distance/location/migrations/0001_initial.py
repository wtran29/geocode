# Generated by Django 2.1.3 on 2018-11-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_name', models.CharField(blank=True, max_length=250)),
                ('loc_address', models.CharField(max_length=255, null=True)),
                ('lat1', models.DecimalField(decimal_places=7, max_digits=1000, null=True)),
                ('lng1', models.DecimalField(decimal_places=7, max_digits=1000, null=True)),
                ('dest_name', models.CharField(blank=True, max_length=250)),
                ('dest_address', models.CharField(max_length=255, null=True)),
                ('lat2', models.DecimalField(decimal_places=7, max_digits=1000, null=True)),
                ('lng2', models.DecimalField(decimal_places=7, max_digits=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
