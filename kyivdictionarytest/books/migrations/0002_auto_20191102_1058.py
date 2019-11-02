# Generated by Django 2.2.6 on 2019-11-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='initials',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booktype',
            name='short_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]