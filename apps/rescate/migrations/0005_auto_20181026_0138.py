# Generated by Django 2.1.2 on 2018-10-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescate', '0004_auto_20181025_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='imagen',
            field=models.FileField(upload_to='media'),
        ),
    ]
