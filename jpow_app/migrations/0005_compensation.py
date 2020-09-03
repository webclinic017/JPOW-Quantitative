# Generated by Django 3.1 on 2020-08-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpow_app', '0004_insider_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticker', models.CharField(max_length=5)),
                ('CeoSalary', models.IntegerField()),
                ('YTDReturn', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]