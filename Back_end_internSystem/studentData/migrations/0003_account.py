# Generated by Django 4.0.3 on 2022-09-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentData', '0002_article_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(default='Empty')),
                ('password', models.TextField(default='Empty')),
            ],
            options={
                'db_table': 'Account',
            },
        ),
    ]