# Generated by Django 5.1.1 on 2024-10-28 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phase3_P2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anaesthsiology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Dermatology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ObsAndGyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Ophthalmology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Orthopaedics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Paediatrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Psychiatry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Radiology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase3_P2.phase3_p2student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
    ]
