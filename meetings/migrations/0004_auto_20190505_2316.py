# Generated by Django 2.0.13 on 2019-05-05 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20190505_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='meetings',
        ),
        migrations.AddField(
            model_name='participant',
            name='meeting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='meeting_category',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='meeting_title',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='meeting_writer',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
    ]
