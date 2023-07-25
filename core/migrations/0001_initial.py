# Generated by Django 4.2.3 on 2023-07-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
    ]
