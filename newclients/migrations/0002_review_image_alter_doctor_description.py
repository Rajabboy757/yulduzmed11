# Generated by Django 4.1.7 on 2023-03-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newclients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
