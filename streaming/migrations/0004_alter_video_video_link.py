# Generated by Django 4.0.4 on 2022-05-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0003_alter_video_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_link',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
