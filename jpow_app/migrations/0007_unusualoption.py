# Generated by Django 3.1 on 2020-08-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpow_app', '0006_auto_20200828_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnusualOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticker', models.CharField(max_length=5)),
                ('Type', models.CharField(max_length=4)),
                ('Strike', models.TextField()),
                ('OpenInterest', models.IntegerField()),
                ('Volume', models.IntegerField()),
                ('ExpirationDate', models.DateField(null=True)),
            ],
        ),
    ]
