# Generated by Django 4.2.3 on 2023-07-11 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogonit', '0004_chategory_post_chategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chategory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='chategory',
            new_name='category',
        ),
    ]