# Generated by Django 5.0.4 on 2024-05-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_cnotents_post_contents'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, upload_to='images/map/')),
                ('map_img', models.ImageField(blank=True, upload_to='images/map/')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('profile_img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
