# Generated by Django 2.2.3 on 2019-07-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0002_auto_20190727_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='comp',
            field=models.CharField(max_length=20, null=True, verbose_name='Complemento'),
        ),
    ]
