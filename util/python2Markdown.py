import markdown # convert markdown 

from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension


class CustomHtmlFormatter(HtmlFormatter):
    def __init__(self, lang_str='', **options):
        super().__init__(**options)
        # lang_str has the value {lang_prefix}{lang}
        # specified by the CodeHilite's options
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'



class Block:
    def __init__(self):
        self.result = []
        
    def codeblock(self, code_block):         
        code = markdown.markdown(
            code_block,
            extensions=[CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)],
        )       
        self.result.append(code)
        
    def titleblock(self, title_block):         
        title = markdown.markdown(
            title_block
            )       
        self.result.append(title)