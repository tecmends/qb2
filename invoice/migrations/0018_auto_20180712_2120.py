# Generated by Django 2.0.5 on 2018-07-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0017_auto_20180712_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfileresults',
            name='total_amount',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]