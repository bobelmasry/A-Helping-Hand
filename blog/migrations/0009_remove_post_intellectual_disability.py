# Generated by Django 4.1.4 on 2023-03-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_diabetes_post_dyslexia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Intellectual_disability',
        ),
    ]