# Generated by Django 4.1 on 2024-03-09 16:51

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'YouTube',
                'ordering': ['-date_added'],
            },
        ),
    ]
