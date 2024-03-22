# Generated by Django 4.1 on 2024-03-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0017_ghanaproject_alter_usaproject_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name_plural': 'project categories',
                'ordering': ['-date_added'],
            },
        ),
        migrations.RenameModel(
            old_name='USAProject',
            new_name='Project',
        ),
        migrations.DeleteModel(
            name='GhanaProject',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_added'], 'verbose_name_plural': 'projects'},
        ),
    ]