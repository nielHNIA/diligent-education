# Generated by Django 3.0.4 on 2020-11-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
