# Generated by Django 2.2.12 on 2020-04-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200227_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='keywords',
            field=models.ManyToManyField(to='projects.Keyword'),
        ),
    ]
