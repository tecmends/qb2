# Generated by Django 2.0.5 on 2018-06-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_auto_20180605_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfileresults',
            name='status',
            field=models.CharField(choices=[('S', 'Success'), ('F', 'Failed'), ('W', 'Warning')], default='S', max_length=50),
        ),
    ]
