# Generated by Django 5.0.4 on 2024-06-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_teachers_teacher_alter_classroom_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='img',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='map_img',
        ),
        migrations.AddField(
            model_name='classroom',
            name='loc_num',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]