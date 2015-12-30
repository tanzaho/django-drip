# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import drip.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Drip Name', unique=True, help_text='A unique name for this drip.')),
                ('enabled', models.BooleanField(default=False)),
                ('marketing', models.BooleanField(help_text='If true, users who have unsubscribed will not get this email. An unsubscribe link will be added automatically to the email footer.', default=True)),
                ('from_email', models.EmailField(max_length=254, null=True, blank=True, help_text='Set a custom from email.')),
                ('from_email_name', models.CharField(max_length=150, null=True, blank=True, help_text='Set a name for a custom from email.')),
                ('subject_template', models.TextField(null=True, blank=True)),
                ('body_html_template', models.TextField(help_text='You will have settings and user in the context.', null=True, blank=True)),
                ('message_class', models.CharField(max_length=120, default='default', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuerySetRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('method_type', models.CharField(max_length=12, default='filter', choices=[('filter', 'Filter'), ('exclude', 'Exclude')])),
                ('field_name', models.CharField(max_length=128, verbose_name='Field name of User')),
                ('lookup_type', models.CharField(max_length=12, default='exact', choices=[('exact', 'exactly'), ('iexact', 'exactly (case insensitive)'), ('contains', 'contains'), ('icontains', 'contains (case insensitive)'), ('regex', 'regex'), ('iregex', 'contains (case insensitive)'), ('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'), ('startswith', 'starts with'), ('endswith', 'starts with'), ('istartswith', 'ends with (case insensitive)'), ('iendswith', 'ends with (case insensitive)')])),
                ('field_value', models.CharField(max_length=255, help_text='Can be anything from a number, to a string. Or, do `now-7 days` or `today+3 days` for fancy timedelta.')),
                ('drip', models.ForeignKey(to='drip.Drip', related_name='queryset_rules')),
            ],
        ),
        migrations.CreateModel(
            name='SentDrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('from_email', models.EmailField(max_length=254, null=True, default=None)),
                ('from_email_name', models.CharField(max_length=150, null=True, default=None)),
                ('drip', models.ForeignKey(to='drip.Drip', related_name='sent_drips')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sent_drips')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('unsubscribe_code', models.CharField(max_length=255, default=drip.models.unique_code, unique=True)),
                ('unsubscribed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
