# Generated by Django 5.0.6 on 2024-08-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('videofile', models.FileField(upload_to='videos/')),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
