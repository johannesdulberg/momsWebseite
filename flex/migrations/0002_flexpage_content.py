# Generated by Django 3.2.15 on 2022-09-25 11:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='add additions Text', required=True))]))], blank=True, null=True),
        ),
    ]
