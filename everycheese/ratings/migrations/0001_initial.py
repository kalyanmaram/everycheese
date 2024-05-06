# Generated by Django 3.1.1 on 2024-03-04 20:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cheeses', '0005_auto_20240304_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('rating', models.IntegerField()),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='cheeses.cheese')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]