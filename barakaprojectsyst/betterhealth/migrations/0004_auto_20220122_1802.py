# Generated by Django 3.2.9 on 2022-01-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betterhealth', '0003_auto_20220122_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='recordinfo',
            name='pid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recordinfo',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
