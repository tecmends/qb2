# Generated by Django 2.0.5 on 2018-05-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_csvfile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='status',
            field=models.CharField(choices=[('Received', 'R'), ('InProgress', 'Q'), ('Completed', 'C'), ('Failed', 'F')], default='R', max_length=50),
        ),
    ]
