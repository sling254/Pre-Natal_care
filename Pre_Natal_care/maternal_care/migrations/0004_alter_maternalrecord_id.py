# Generated by Django 3.2.6 on 2021-08-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maternal_care', '0003_auto_20210803_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maternalrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
