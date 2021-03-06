# Generated by Django 3.2.4 on 2021-06-12 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_questions', to='quiz.exam')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('is_answer', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_question', to='quiz.question')),
            ],
            options={
                'verbose_name': 'Question Choice',
                'verbose_name_plural': 'Question Choices',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_choice', to='quiz.questionchoice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_question', to='quiz.question')),
            ],
            options={
                'verbose_name': 'Question Answer',
                'verbose_name_plural': 'Question Answers',
                'ordering': ('created',),
            },
        ),
    ]
