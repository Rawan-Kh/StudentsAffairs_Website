# Generated by Django 4.0.4 on 2022-05-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='CourseID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
