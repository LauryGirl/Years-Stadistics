# Generated by Django 4.0.1 on 2022-02-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('professor', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=128)),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('blocked', models.BooleanField(default=False)),
                ('verification_code', models.IntegerField(default=0)),
                ('verification_code_created_date', models.DateTimeField(blank=True, null=True)),
                ('roles', models.ManyToManyField(related_name='users', to='user.Role')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-id'],
            },
        ),
    ]