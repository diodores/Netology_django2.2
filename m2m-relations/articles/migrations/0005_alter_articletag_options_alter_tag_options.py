# Generated by Django 4.0 on 2022-06-21 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'ordering': ['tag'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]