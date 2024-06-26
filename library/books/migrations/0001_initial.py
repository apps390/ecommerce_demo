# Generated by Django 5.0.2 on 2024-03-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
                ('book_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('cover', models.ImageField(upload_to='books/image')),
                ('pdf', models.FileField(upload_to='books/pdf')),
            ],
        ),
    ]
