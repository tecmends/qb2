# Generated by Django 2.0.5 on 2018-07-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_csvfile_batch_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfileresults',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]