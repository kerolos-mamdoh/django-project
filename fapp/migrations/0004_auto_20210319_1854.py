# Generated by Django 3.1.7 on 2021-03-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0003_auto_20210317_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='addproject',
            name='id_user',
            field=models.IntegerField(null=True),
        ),
    ]
