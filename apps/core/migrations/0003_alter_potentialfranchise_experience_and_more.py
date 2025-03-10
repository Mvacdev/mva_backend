# Generated by Django 4.2.19 on 2025-03-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_potentialfranchise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialfranchise',
            name='experience',
            field=models.TextField(help_text='Expérience professionnelle (secteurs pertinents) *', max_length=2000),
        ),
        migrations.AlterField(
            model_name='potentialfranchise',
            name='message',
            field=models.TextField(blank=True, help_text='Message (facultatif)', max_length=5000),
        ),
    ]
