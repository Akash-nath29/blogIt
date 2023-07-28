# Generated by Django 4.2.3 on 2023-07-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogonit', '0009_alter_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]