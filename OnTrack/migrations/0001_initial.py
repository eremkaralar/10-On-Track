# Generated by Django 3.1.2 on 2020-12-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalname', models.CharField(max_length=200)),
                ('goalstepset', models.IntegerField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
