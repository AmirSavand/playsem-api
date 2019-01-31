# Generated by Django 2.1.5 on 2019-01-31 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20190201_0143'),
        ('song', '0002_song_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='party.PartyCategory'),
        ),
    ]
