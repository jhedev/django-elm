from django import template

from subprocess import Popen, PIPE
import re

from ..settings import ELM_COMPILER_EXECUTABLE

register = template.Library()

@register.tag(name="elminline")
def do_elm_inline(parser,token):
    nodelist = parser.parse(('endelminline',))
    parser.delete_first_token()
    return ElmNode(nodelist)

class ElmNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    
    def compile(self,source):
        process = Popen(ELM_COMPILER_EXECUTABLE,shell=True, stdin=PIPE, stdout=PIPE)
        (javascript,err) = process.communicate(input=self.nodelist.render(source))
        if not err:
            return javascript
        return ""

    def render(self, context):
        return '<script type="text/javascript">' + self.compile(context) + '</script>'


