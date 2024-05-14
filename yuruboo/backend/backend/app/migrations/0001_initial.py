# Generated by Django 5.0.4 on 2024-05-14 05:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pos_lat', models.FloatField(help_text='募集場所_緯度')),
                ('pos_lng', models.FloatField(help_text='募集場所_経度')),
                ('body', models.CharField(help_text='本文', max_length=1024)),
                ('num_participant', models.IntegerField(help_text='人数')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='募集開始日時')),
                ('start_time', models.DateTimeField(help_text='集合時刻')),
                ('budget', models.CharField(choices=[('FREE', '無料'), ('UNDER_1000', '~ 1,000円'), ('UNDER_3000', '1,000円 ~ 3,000円'), ('UNDER_5000', '3,000円 ~ 5,000円'), ('OVER_5000', '5,000円 ~'), ('UNDECIDED', '未定')], default='UNDECIDED', help_text='予算', max_length=10)),
                ('title', models.CharField(default='(タイトル未設定)', help_text='タイトル', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(help_text='ジャンル名', max_length=255, primary_key=True, serialize=False)),
                ('label', models.CharField(help_text='ラベル', max_length=255)),
                ('icon', models.URLField(help_text='アイコンURL', max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.CharField(help_text='本文', max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='投稿日時')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('count', models.IntegerField(help_text='本数')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='参加日時')),
            ],
        ),
    ]
