# Generated by Django 2.1.10 on 2019-11-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contract', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ('-create_time',), 'verbose_name_plural': '合同信息'},
        ),
    ]
