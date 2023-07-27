# Generated by Django 4.2.3 on 2023-07-25 10:54

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
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('date_of_expense', models.DateField()),
                ('category', models.CharField(choices=[('Health', 'Health'), ('Electronics', 'Electronics'), ('Travel', 'Travel'), ('Education', 'Education'), ('Books', 'Books'), ('Others', 'Others')], max_length=15)),
                ('description', models.TextField()),
                ('amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
