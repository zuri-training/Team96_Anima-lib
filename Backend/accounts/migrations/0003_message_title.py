# Generated by Django 4.1 on 2022-08-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_fk_message_image_rename_fk_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
