# Generated by Django 2.0.7 on 2018-12-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
