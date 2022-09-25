""" STREAMFIELDS"""

from wagtail.core import blocks
from wagtail.core.blocks import URLBlock, PageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your Title")
    text = blocks.TextBlock(required=True, help_text="add additions Text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class Navbar(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(
        required=False, help_text="If the button page above is selected, that will be used first.")
    item = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False,
             help_text="If the button page above is selected, that will be used first.")),
        ])
    )

    class Meta:
        icon = "edit"
        label = "Navigationsleite"
        template = "streams/Navbar.html"
