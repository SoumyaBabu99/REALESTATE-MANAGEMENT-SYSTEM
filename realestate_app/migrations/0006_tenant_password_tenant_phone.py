# Generated by Django 5.0.1 on 2024-01-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0005_tenant_document_proofs'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
