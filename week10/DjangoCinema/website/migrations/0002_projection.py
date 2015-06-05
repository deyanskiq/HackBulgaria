# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('projection_type', models.CharField(max_length=10)),
                ('when', models.DateTimeField()),
                ('movie', models.ForeignKey(to='website.Movie')),
            ],
        ),
    ]
