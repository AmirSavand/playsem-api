# Generated by Django 3.0 on 2020-02-11 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('party', '0008_auto_20200103_2044'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('song', '0005_auto_20191229_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True)),
                ('when', models.TimeField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.Party')),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='song.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DJ',
                'verbose_name_plural': 'DJs',
                'unique_together': {('user', 'party')},
            },
        ),
        migrations.CreateModel(
            name='DjUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj.Dj')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DJ user',
                'verbose_name_plural': 'DJ users',
                'unique_together': {('dj', 'user')},
            },
        ),
    ]
