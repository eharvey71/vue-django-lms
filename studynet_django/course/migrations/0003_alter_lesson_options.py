# Generated by Django 4.2 on 2023-06-16 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_lesson_alter_category_options_quiz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': 'Lessons'},
        ),
    ]