# Generated by Django 4.1 on 2024-03-22 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0018_projectcategory_rename_usaproject_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundation.projectcategory'),
        ),
    ]
