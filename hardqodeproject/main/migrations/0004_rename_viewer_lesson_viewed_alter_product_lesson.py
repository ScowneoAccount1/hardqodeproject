# Generated by Django 4.2.5 on 2023-09-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_lesson_product_product_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='viewer',
            new_name='viewed',
        ),
        migrations.AlterField(
            model_name='product',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='main.lesson'),
        ),
    ]
