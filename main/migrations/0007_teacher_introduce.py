# Generated by Django 5.0.4 on 2024-06-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='introduce',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]