# Generated by Django 5.0.4 on 2024-05-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='ContactInfo name')),
                ('desc', models.TextField(verbose_name='ContactInfo text')),
                ('address', models.TextField(verbose_name='ContactInfo address')),
                ('phone1', models.CharField(max_length=30, verbose_name='ContactInfo phone1')),
                ('phone2', models.CharField(max_length=30, verbose_name='ContactInfo phone2')),
                ('email', models.EmailField(max_length=254, verbose_name='ContactInfo email')),
                ('fb', models.TextField(blank=True, verbose_name='Person fb')),
                ('insta', models.TextField(blank=True, verbose_name='Person insta')),
            ],
        ),
    ]
