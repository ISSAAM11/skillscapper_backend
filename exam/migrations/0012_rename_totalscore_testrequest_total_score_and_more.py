# Generated by Django 5.1.6 on 2025-02-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_testrequest_id_exam_alter_testrequest_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testrequest',
            old_name='totalScore',
            new_name='total_score',
        ),
        migrations.AddField(
            model_name='testrequest',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
