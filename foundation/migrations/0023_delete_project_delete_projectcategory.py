# Generated by Django 4.1 on 2024-03-25 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0022_projectcategory_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
    ]
