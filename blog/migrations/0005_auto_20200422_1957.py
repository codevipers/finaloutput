# Generated by Django 3.0.5 on 2020-04-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='reply',
            name='replyimage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
