# Generated by Django 5.0.6 on 2024-07-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBIKE', '0004_alter_usuario_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
    ]