# Generated by Django 3.1.7 on 2021-05-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=10)),
            ],
        ),
    ]