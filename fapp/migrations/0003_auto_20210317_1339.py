# Generated by Django 3.1.7 on 2021-03-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0003_adapt_max_tag_length'),
        ('fapp', '0002_addproject_total_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='photos', to='tagging.Tag'),
        ),
    ]
