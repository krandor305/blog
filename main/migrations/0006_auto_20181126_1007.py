# Generated by Django 2.1.3 on 2018-11-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_article_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(max_length=300),
        ),
    ]