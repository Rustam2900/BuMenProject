# Generated by Django 4.2 on 2024-07-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_news_banner_alter_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='link',
            field=models.URLField(null=True),
        ),
    ]