# Generated by Django 3.1.2 on 2020-12-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnTrack', '0003_auto_20201207_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='goals',
        ),
        migrations.AddField(
            model_name='goals',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OnTrack.customer'),
        ),
    ]
