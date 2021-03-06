# Generated by Django 2.2.8 on 2020-03-21 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acAppYouTube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='Alumno',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
