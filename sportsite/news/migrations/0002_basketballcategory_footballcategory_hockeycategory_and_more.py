# Generated by Django 4.1.7 on 2023-03-17 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketballCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='FootballCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='HockeyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='basketball_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.basketballcategory', verbose_name='Чемпионат'),
        ),
        migrations.AddField(
            model_name='article',
            name='football_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.footballcategory', verbose_name='Чемпионат'),
        ),
        migrations.AddField(
            model_name='article',
            name='hockey_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.hockeycategory', verbose_name='Чемпионат'),
        ),
    ]
