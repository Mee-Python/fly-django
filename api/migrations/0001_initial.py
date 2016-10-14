# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-24 18:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Badge'), (2, 'Goal Badge'), (3, 'Education Badge'), (4, 'Resource Badge')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('icon', models.CharField(blank=True, max_length=31, null=True)),
                ('colour', models.CharField(blank=True, max_length=31, null=True)),
                ('level', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('title_en', models.CharField(blank=True, max_length=63, null=True)),
                ('title_fr', models.CharField(blank=True, max_length=63, null=True)),
                ('title_es', models.CharField(blank=True, max_length=63, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('description_en', models.CharField(blank=True, max_length=511, null=True)),
                ('description_fr', models.CharField(blank=True, max_length=511, null=True)),
                ('description_es', models.CharField(blank=True, max_length=511, null=True)),
                ('has_xp_requirement', models.BooleanField(default=True)),
                ('required_xp', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'db_table': 'fly_badges',
            },
        ),
        migrations.CreateModel(
            name='BannedDomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=63, unique=True)),
                ('banned_on', models.DateField(auto_now_add=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=127, null=True)),
            ],
            options={
                'db_table': 'fly_banned_domains',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BannedIP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.GenericIPAddressField(db_index=True, unique=True)),
                ('banned_on', models.DateField(auto_now_add=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=127, null=True)),
            ],
            options={
                'db_table': 'fly_banned_ips',
                'ordering': ('address',),
            },
        ),
        migrations.CreateModel(
            name='BannedWord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(db_index=True, max_length=63, unique=True)),
                ('banned_on', models.DateField(auto_now_add=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=127, null=True)),
            ],
            options={
                'db_table': 'fly_banned_words',
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Savings'), (2, 'Credit'), (3, 'Goal')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('image', models.CharField(blank=True, max_length=63, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('title_en', models.CharField(blank=True, max_length=63, null=True)),
                ('title_fr', models.CharField(blank=True, max_length=63, null=True)),
                ('title_es', models.CharField(blank=True, max_length=63, null=True)),
                ('summary', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_en', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('summary_es', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('description_en', models.CharField(blank=True, max_length=511, null=True)),
                ('description_fr', models.CharField(blank=True, max_length=511, null=True)),
                ('description_es', models.CharField(blank=True, max_length=511, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('duration', models.PositiveSmallIntegerField(choices=[(5, '5 Minutes'), (30, '30 Minutes'), (60, '1 Hour')], default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(60)])),
                ('awarded_xp', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('has_prerequisites', models.BooleanField(db_index=True, default=False)),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='_course_prerequisites_+', to='api.Course')),
            ],
            options={
                'db_table': 'fly_courses',
            },
        ),
        migrations.CreateModel(
            name='CreditGoal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('goal_type', models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('unlocks', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.BooleanField(db_index=True, default=False)),
                ('was_accomplished', models.BooleanField(db_index=True, default=False)),
                ('earned_xp', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('points', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(850)])),
                ('times', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('period', models.PositiveSmallIntegerField(choices=[(1, 'Weeks'), (2, 'Months')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_credit_goals',
            },
        ),
        migrations.CreateModel(
            name='EnrolledCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('final_mark', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_enrolled_courses',
            },
        ),
        migrations.CreateModel(
            name='FinalGoal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('goal_type', models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('unlocks', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.BooleanField(db_index=True, default=False)),
                ('was_accomplished', models.BooleanField(db_index=True, default=False)),
                ('earned_xp', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('for_want', models.PositiveSmallIntegerField(choices=[(1, 'House'), (2, 'Business'), (3, 'Vacation'), (4, 'Retirement'), (5, 'General Savings'), (6, 'Other')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('for_other_want', models.CharField(blank=True, default='', max_length=63, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_final_goals',
            },
        ),
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('upload_id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_date', models.DateField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_image_uploads',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('xp', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
                ('xp_percent', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('wants_newsletter', models.BooleanField(default=False)),
                ('wants_goal_notify', models.BooleanField(default=False)),
                ('wants_course_notify', models.BooleanField(default=False)),
                ('wants_resource_notify', models.BooleanField(default=False)),
                ('badges', models.ManyToManyField(blank=True, related_name='fly_user_badges', to='api.Badge')),
                ('courses', models.ManyToManyField(blank=True, related_name='fly_user_enrolled_courses', to='api.EnrolledCourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_mes',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Level Up Notifiction'), (2, 'New Badge Notification'), (3, 'Custom Notification')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('title', models.CharField(blank=True, max_length=511, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('badge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_notifications',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('num', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('text', models.CharField(blank=True, max_length=511, null=True)),
                ('text_en', models.CharField(blank=True, max_length=511, null=True)),
                ('text_fr', models.CharField(blank=True, max_length=511, null=True)),
                ('text_es', models.CharField(blank=True, max_length=511, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Open-Ended'), (2, 'Partial'), (3, 'All-or-None')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('a', models.CharField(blank=True, max_length=255, null=True)),
                ('a_en', models.CharField(blank=True, max_length=255, null=True)),
                ('a_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('a_es', models.CharField(blank=True, max_length=255, null=True)),
                ('a_is_correct', models.BooleanField(default=False)),
                ('b', models.CharField(blank=True, max_length=255, null=True)),
                ('b_en', models.CharField(blank=True, max_length=255, null=True)),
                ('b_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('b_es', models.CharField(blank=True, max_length=255, null=True)),
                ('b_is_correct', models.BooleanField(default=False)),
                ('c', models.CharField(blank=True, max_length=255, null=True)),
                ('c_en', models.CharField(blank=True, max_length=255, null=True)),
                ('c_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('c_es', models.CharField(blank=True, max_length=255, null=True)),
                ('c_is_correct', models.BooleanField(default=False)),
                ('d', models.CharField(blank=True, max_length=255, null=True)),
                ('d_en', models.CharField(blank=True, max_length=255, null=True)),
                ('d_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('d_es', models.CharField(blank=True, max_length=255, null=True)),
                ('d_is_correct', models.BooleanField(default=False)),
                ('e', models.CharField(blank=True, max_length=255, null=True)),
                ('e_en', models.CharField(blank=True, max_length=255, null=True)),
                ('e_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('e_es', models.CharField(blank=True, max_length=255, null=True)),
                ('e_is_correct', models.BooleanField(default=False)),
                ('f', models.CharField(blank=True, max_length=255, null=True)),
                ('f_en', models.CharField(blank=True, max_length=255, null=True)),
                ('f_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('f_es', models.CharField(blank=True, max_length=255, null=True)),
                ('f_is_correct', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fly_questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Open-Ended'), (2, 'Partial'), (3, 'All-or-None')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('a', models.BooleanField(default=False)),
                ('b', models.BooleanField(default=False)),
                ('c', models.BooleanField(default=False)),
                ('d', models.BooleanField(default=False)),
                ('e', models.BooleanField(default=False)),
                ('f', models.BooleanField(default=False)),
                ('mark', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question')),
            ],
            options={
                'db_table': 'fly_question_submissions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('title_en', models.CharField(blank=True, max_length=63, null=True)),
                ('title_fr', models.CharField(blank=True, max_length=63, null=True)),
                ('title_es', models.CharField(blank=True, max_length=63, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('description_en', models.CharField(blank=True, max_length=511, null=True)),
                ('description_fr', models.CharField(blank=True, max_length=511, null=True)),
                ('description_es', models.CharField(blank=True, max_length=511, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
            options={
                'db_table': 'fly_quizzes',
            },
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('final_mark', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_quiz_submissions',
            },
        ),
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=127)),
                ('title_en', models.CharField(max_length=127, null=True)),
                ('title_fr', models.CharField(max_length=127, null=True)),
                ('title_es', models.CharField(max_length=127, null=True)),
                ('url', models.URLField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Social Media'), (2, 'Blogs'), (3, 'Other Cool Apps')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
            ],
            options={
                'db_table': 'fly_resource_links',
            },
        ),
        migrations.CreateModel(
            name='SavingsGoal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('goal_type', models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('unlocks', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.BooleanField(db_index=True, default=False)),
                ('was_accomplished', models.BooleanField(db_index=True, default=False)),
                ('earned_xp', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('times', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('period', models.PositiveSmallIntegerField(choices=[(1, 'Weeks'), (2, 'Months')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_savings_goals',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Level Up Share'), (2, 'New Badge Share'), (3, 'Custom Share')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('custom_title', models.CharField(blank=True, max_length=511, null=True)),
                ('custom_description', models.CharField(blank=True, max_length=511, null=True)),
                ('custom_url', models.URLField(blank=True, null=True)),
                ('notification_id', models.PositiveIntegerField(blank=True)),
                ('badge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_shares',
            },
        ),
        migrations.CreateModel(
            name='XPLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=31, null=True)),
                ('num', models.PositiveSmallIntegerField(choices=[(5, '5 Minutes'), (30, '30 Minutes'), (60, '1 Hour')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('min_xp', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('max_xp', models.PositiveSmallIntegerField(default=25, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'db_table': 'fly_xp_levels',
            },
        ),
        migrations.AddField(
            model_name='share',
            name='xplevel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.XPLevel'),
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quiz'),
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quiz'),
        ),
        migrations.AddField(
            model_name='notification',
            name='xplevel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.XPLevel'),
        ),
        migrations.AddField(
            model_name='me',
            name='xplevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.XPLevel'),
        ),
        migrations.CreateModel(
            name='OrderedCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('created',),
            },
            bases=('api.course',),
        ),
        migrations.CreateModel(
            name='OrderedCreditGoal',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('-created',),
            },
            bases=('api.creditgoal',),
        ),
        migrations.CreateModel(
            name='OrderedFinalGoal',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('-created',),
            },
            bases=('api.finalgoal',),
        ),
        migrations.CreateModel(
            name='OrderedQuestion',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('num',),
            },
            bases=('api.question',),
        ),
        migrations.CreateModel(
            name='OrderedSavingsGoal',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('-created',),
            },
            bases=('api.savingsgoal',),
        ),
    ]