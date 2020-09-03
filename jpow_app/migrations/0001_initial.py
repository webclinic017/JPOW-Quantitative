# Generated by Django 3.1 on 2020-08-24 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('PositiveSentiment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SPY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('closePrice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]