# Generated by Django 4.0 on 2022-06-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=25, verbose_name='Предмет'),
        ),
    ]