# Generated by Django 4.1.5 on 2023-01-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_remove_form_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('fname', models.CharField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
