# Generated by Django 3.2.5 on 2021-07-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='national_id',
            field=models.FileField(upload_to='images/'),
        ),
    ]
