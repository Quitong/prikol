# Generated by Django 3.2.25 on 2024-05-27 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_answer_question_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='to_quiz',
        ),
        migrations.AddField(
            model_name='answer',
            name='to_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.question'),
            preserve_default=False,
        ),
    ]
