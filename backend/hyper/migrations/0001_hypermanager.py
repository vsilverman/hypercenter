# Generated by Django 3.0.6 on 2020-06-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hyper', '0000_create_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='HyperManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('hv_type', models.CharField(choices=[('vcenter', 'Vcenter'), ('hyperv', 'HyperV')], default='vcenter', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(default='', max_length=100)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
    ]