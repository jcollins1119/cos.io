# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambassadors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('original_image_width', models.PositiveIntegerField(null=True)),
                ('original_image_height', models.PositiveIntegerField(null=True)),
                ('thumb_image_width', models.PositiveIntegerField(null=True)),
                ('thumb_image_height', models.PositiveIntegerField(null=True)),
                ('image', image_cropping.fields.ImageCropField(upload_to=b'uploaded_images')),
                (b'mini_image', image_cropping.fields.ImageRatioField(b'image', '0x0', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name='mini image')),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': ' COS Ambassadors ',
            },
        ),
    ]
