# Generated by Django 3.2.4 on 2021-07-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0003_alter_project_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttag',
            name='bg_color',
            field=models.CharField(default='#4af', max_length=6, verbose_name='Background Color'),
            preserve_default=False,
        ),
    ]
