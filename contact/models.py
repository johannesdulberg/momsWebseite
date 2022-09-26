from django.db import models

# Create your models here.

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from streams import blocks


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm, Page):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    content = StreamField(
        [
            ("Navigationsleiste", blocks.Navbar()),
            ("Header", blocks.Header()),
            ("ImgAndText", blocks.ImgAndText()),
            ("TextAndSubtext", blocks.TextAndSubtext()),
            ("BigImg", blocks.BigImg()),
            ("Footer", blocks.Footer()),
        ],
        null=True,
        blank=True
    )

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel("content"),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
        StreamFieldPanel("content"),
    ]
