# Generated by Django 2.1.3 on 2018-11-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20181117_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='location',
            name='title',
        ),
        migrations.AddField(
            model_name='location',
            name='destination',
            field=models.CharField(choices=[('from', 'From'), ('to', 'To')], default='from', max_length=120),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=1000, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.DeleteModel(
            name='Coordinate',
        ),
    ]