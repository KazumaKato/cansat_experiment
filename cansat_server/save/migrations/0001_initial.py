# Generated by Django 4.0.2 on 2022-02-04 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapturedImage',
            fields=[
                ('image', models.ImageField(upload_to='images')),
                ('distance', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
