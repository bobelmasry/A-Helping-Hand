# Generated by Django 4.1.4 on 2023-03-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content_alter_post_short_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='answer',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
