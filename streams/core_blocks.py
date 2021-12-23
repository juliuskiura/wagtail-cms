from wagtail.core import blocks


class HeadingAndParagraphBlocks(blocks.StructBlock):
   
    span_units_once = blocks.CharBlock(required=True, help_text='Add a header text')
    span_unit_number = blocks.CharBlock(
        required=True, help_text='Add a header text')
    heading = blocks.CharBlock(required=True, help_text='Add a header text')
    paragraph = blocks.TextBlock(required=True, help_text = 'Add body text')

    class Meta:
        template = 'streams/heading_and_paragraph.html'
        icon = 'edit'
        label = 'Heading & Body'


class ParagraphBlocks(blocks.RichTextBlock):
    class Meta:
        template = 'streams/rich_para_block.html'
        icon = 'edit'
        label = 'Body Content'
