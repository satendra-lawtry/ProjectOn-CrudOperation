# Generated by Django 4.0.4 on 2022-05-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('contact', models.BigIntegerField(null=True)),
            ],
        ),
    ]
