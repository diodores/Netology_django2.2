# Generated by Django 4.0 on 2022-06-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articletag_alter_article_tags_articletag_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]