# Generated by Django 2.1.3 on 2020-06-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='storage_url',
        ),
    ]
