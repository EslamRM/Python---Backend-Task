# Generated by Django 4.1.5 on 2023-01-17 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=200)),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('image', models.URLField()),
                ('brand', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(db_index=True, decimal_places=3, default=0, max_digits=10)),
                ('quantity', models.IntegerField(db_index=True, default=1)),
                ('rating', models.FloatField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('image', models.URLField()),
                ('brand', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(db_index=True, decimal_places=3, default=0, max_digits=10)),
                ('quantity', models.IntegerField(db_index=True, default=1)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
