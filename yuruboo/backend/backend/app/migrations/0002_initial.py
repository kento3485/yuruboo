# Generated by Django 5.0.4 on 2024-05-12 12:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='host',
            field=models.ForeignKey(help_text='募集者', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gathering',
            name='genre',
            field=models.ForeignKey(help_text='ジャンル', on_delete=django.db.models.deletion.PROTECT, to='app.genre'),
        ),
        migrations.AddField(
            model_name='message',
            name='gathering',
            field=models.ForeignKey(help_text='募集', on_delete=django.db.models.deletion.PROTECT, to='app.gathering'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(help_text='送り手', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ownership',
            name='owner',
            field=models.ForeignKey(help_text='所有者', on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ownership',
            name='presenter',
            field=models.ForeignKey(help_text='贈呈者', on_delete=django.db.models.deletion.PROTECT, related_name='presenter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participation',
            name='gathering',
            field=models.ForeignKey(help_text='募集', on_delete=django.db.models.deletion.PROTECT, to='app.gathering'),
        ),
        migrations.AddField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(help_text='参加者', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
