# Generated by Django 5.0.4 on 2024-04-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_msg_contact_massage_alter_blog_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='publish_on',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
