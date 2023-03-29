# Generated by Django 4.1.7 on 2023-03-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_basketballcategory_footballcategory_hockeycategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketballcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Бакстебольный чемпионат'),
        ),
        migrations.AlterField(
            model_name='footballcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Футбольный Чемпионат'),
        ),
        migrations.AlterField(
            model_name='hockeycategory',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Хоккейный чемпионат'),
        ),
    ]