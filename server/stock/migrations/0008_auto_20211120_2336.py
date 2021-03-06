# Generated by Django 3.2.5 on 2021-11-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_initialized',
            field=models.BooleanField(default=False, verbose_name='初期登録済み'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(max_length=20, null=True, verbose_name='公開名'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='screen_name',
            field=models.CharField(max_length=12, null=True, unique=True, verbose_name='スクリーンネーム'),
        ),
    ]
