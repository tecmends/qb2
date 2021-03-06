# Generated by Django 2.0.5 on 2018-06-05 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import invoice.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0005_auto_20180531_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldMappings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping', django_mysql.models.JSONField(default=invoice.models.default_mapping)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='status',
            field=models.CharField(choices=[('Received', 'R'), ('InProgress', 'Q'), ('Completed', 'C'), ('Failed', 'F')], default='R', max_length=50),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='upload_file',
            field=models.FileField(upload_to=invoice.models.CsvFile.uid_upload_to),
        ),
    ]
