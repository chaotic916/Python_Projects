# Generated by Django 3.2.23 on 2023-12-10 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20231205_1311'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='item.item'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='members',
            field=models.ManyToManyField(related_name='conversation', to=settings.AUTH_USER_MODEL),
        ),
    ]