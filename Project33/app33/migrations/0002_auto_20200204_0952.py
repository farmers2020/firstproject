# Generated by Django 3.0.2 on 2020-02-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app33', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='studentid',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='courseid',
            field=models.ManyToManyField(to='app33.CourseModel'),
        ),
    ]
