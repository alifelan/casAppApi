# Generated by Django 2.2 on 2019-04-28 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField()),
                ('time', models.TimeField()),
            ],
            options={
                'unique_together': {('day', 'time')},
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField()),
                ('semester', models.CharField(max_length=6)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='casApp.Class')),
                ('dates', models.ManyToManyField(related_name='groups', to='casApp.Date')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('maps', models.TextField()),
                ('photo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('mat', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='casApp.Casa')),
                ('enrolled_in', models.ManyToManyField(related_name='students', to='casApp.Group')),
                ('events', models.ManyToManyField(related_name='events', to='casApp.Event')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(related_name='groups', to='casApp.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('group_number', 'class_id', 'semester')},
        ),
    ]
