# Generated by Django 4.0.1 on 2022-01-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardgame',
            name='mode',
            field=models.CharField(choices=[('작은 수', '작은 수'), ('큰 수', '큰 수')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cardgame',
            name='status',
            field=models.CharField(choices=[('진행중', '진행중'), ('끝', '끝')], max_length=20),
        ),
    ]
