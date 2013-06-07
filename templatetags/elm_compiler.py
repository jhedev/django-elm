from django import template

from subprocess import Popen, PIPE
import re

register = template.Library()

@register.tag(name="elm")
def do_elm(parser,token):
    nodelist = parser.parse(('endelm',))
    parser.delete_first_token()
    return ElmNode(nodelist)

class ElmNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    
    def compile(self,source):
        process = Popen('elmToHtml',shell=True, stdin=PIPE, stdout=PIPE)
        (javascript,err) = process.communicate(input=self.nodelist.render(source))
        if not err:
            return javascript
        return ""

    def render(self, context):
        return '<script type="text/javascript">' + self.compile(context) + '</script>'


