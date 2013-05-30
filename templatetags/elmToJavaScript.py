from django import template

from subprocess import Popen, PIPE

register = template.Library()

def do_elm(parser,token):
    nodelist = parser.parse(('endelm',))
    parser.delete_first_token()
    return ElmNode(nodelist)

class ElmNode(template.Node)
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        process = Popen(['runghc', 'elmToHtml'], stdin=PIPE)
        javascript = process.communicate(input=self.nodelist.render(context))
        return '<script>' + javascript + '</script>'


register.tag('elm',do_elm)
