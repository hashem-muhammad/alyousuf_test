# Generated by Django 3.2 on 2022-05-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_alter_post_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
