# Generated by Django 3.0 on 2022-03-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('later', 'later'), ('doing', 'doing'), ('done', 'done')], max_length=255)),
            ],
        ),
    ]