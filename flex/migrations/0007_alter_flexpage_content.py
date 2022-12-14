# Generated by Django 3.2.15 on 2022-09-25 15:43

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Navigationsleiste', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('Header', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('SUBTITLE', wagtail.core.blocks.TextBlock(required=True)), ('BUTTON', wagtail.core.blocks.TextBlock(required=False)), ('MasterImage', wagtail.images.blocks.ImageChooserBlock(required=True))]))], blank=True, null=True),
        ),
    ]
