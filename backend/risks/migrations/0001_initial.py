# Generated by Django 2.1.1 on 2018-09-19 06:48

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('data_type', models.IntegerField(choices=[(1, 'Text'), (2, 'Number'), (3, 'Date'), (4, 'Choice')])),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='insuranceschema',
            name='insurer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='risks.Insurer'),
        ),
        migrations.AddField(
            model_name='insurancerecord',
            name='insurer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='risks.Insurer'),
        ),
        migrations.AddField(
            model_name='insurancerecord',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='risks.InsuranceSchema'),
        ),
        migrations.AddField(
            model_name='insurancefield',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fields', to='risks.InsuranceSchema'),
        ),
    ]
