# Generated by Django 4.1.7 on 2023-03-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='walletDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder', models.CharField(max_length=25)),
                ('card_no', models.CharField(max_length=19)),
                ('purse_amt', models.IntegerField()),
            ],
        ),
    ]
