# Generated by Django 4.2.1 on 2023-05-10 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
    ]