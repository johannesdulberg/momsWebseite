from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks


class HomePage(Page):
    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("Navigationsleiste", blocks.Navbar()),
            ("Header", blocks.Header()),
            ("ImgAndText", blocks.ImgAndText()),
            ("TextAndSubtext", blocks.TextAndSubtext()),
            ("BigImg", blocks.BigImg()),
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
