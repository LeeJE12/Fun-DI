# Generated by Django 5.1 on 2024-08-23 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubname', models.CharField(max_length=100, unique=True)),
                ('clubpw', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('budget', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='fundi.club')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipFeeEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundi.event')),
                ('money', models.IntegerField()),
            ],
            bases=('fundi.event',),
        ),
        migrations.CreateModel(
            name='NoFeeEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundi.event')),
                ('money', models.IntegerField()),
            ],
            bases=('fundi.event',),
        ),
        migrations.CreateModel(
            name='PartialFeeEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundi.event')),
                ('money', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
            bases=('fundi.event',),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=100)),
                ('memberdues', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='fundi.club')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events', to='fundi.member'),
        ),
        migrations.CreateModel(
            name='MoneyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(blank=True, max_length=200, null=True)),
                ('money', models.IntegerField(blank=True, null=True)),
                ('eventid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventlist', to='fundi.event')),
            ],
        ),
    ]
