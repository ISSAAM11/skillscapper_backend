# Generated by Django 5.1.6 on 2025-02-15 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_rename_test_type_exam_test_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_limit', models.DateField(blank=True, null=True)),
                ('totalScore', models.IntegerField(default=0)),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.exam')),
            ],
        ),
    ]
