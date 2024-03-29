# Generated by Django 2.2.3 on 2019-11-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classify', '0002_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooperationState', models.CharField(max_length=10, unique=True, verbose_name='合作状态')),
                ('Note', models.CharField(blank=True, max_length=10, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '合作状态',
                'db_table': 'cooperationstate',
            },
        ),
    ]
