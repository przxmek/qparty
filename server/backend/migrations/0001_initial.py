# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('service_id', models.CharField(max_length=50)),
                ('voting_result', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('downvoted_songs', models.ManyToManyField(related_name='downvoters', to='backend.Song')),
                ('party', models.ForeignKey(to='backend.Party')),
                ('session', models.ForeignKey(to='sessions.Session')),
                ('upvoted_songs', models.ManyToManyField(related_name='upvoters', to='backend.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='party',
            name='songs',
            field=models.ManyToManyField(to='backend.Song'),
            preserve_default=True,
        ),
    ]
