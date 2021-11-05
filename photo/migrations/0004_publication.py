# Generated by Django 3.2.8 on 2021-11-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_photo_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('albums', models.ManyToManyField(to='photo.Album')),
            ],
        ),
    ]