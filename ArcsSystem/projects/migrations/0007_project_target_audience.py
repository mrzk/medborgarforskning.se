# Generated by Django 3.0.3 on 2020-02-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='target_audience',
            field=models.CharField(default='Empty', max_length=5000),
        ),
    ]