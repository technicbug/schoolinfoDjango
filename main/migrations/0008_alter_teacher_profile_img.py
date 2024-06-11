

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_teacher_introduce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='images/profile'),
        ),
    ]
