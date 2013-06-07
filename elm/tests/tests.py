from unittest import main, TestCase

import os

os.environ['DJANGO_SETTINGS_MODULE'] = "elm.tests.django_settings"

from django.template.base import Template
from django.template.context import RequestContext
from django.http import HttpRequest

class ElmCompileTestCase(TestCase):
    def _get_request_context(self):
        return RequestContext(HttpRequest())    

    def test_elm_inline(self):
        template = Template("""
            {% load elm_compiler %}
            {% elminline %}main = plainText "Hello"{% endelminline %}""")
        render = """<script type="text/javascript">
  Elm.Main = function(elm){
  var N = Elm.Native, _N = N.Utils(elm), _L = N.List(elm), _E = N.Error(elm), _str = N.JavaScript(elm).toString;
  var $op = {};
  var _ = Elm.Text(elm); var Text = _; var hiding={link:1, color:1, height:1}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Prelude(elm); var Prelude = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Signal(elm); var Signal = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.List(elm); var List = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Maybe(elm); var Maybe = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Time(elm); var Time = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Graphics.Element(elm); var Graphics = Graphics||{};Graphics.Element = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Color(elm); var Color = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var _ = Elm.Graphics.Collage(elm); var Graphics = Graphics||{};Graphics.Collage = _; var hiding={}; for(var k in _){if(k in hiding)continue;eval('var '+k+'=_["'+k+'"]')}
  var main_0 = plainText(_str('Hello'));
  elm.Native = elm.Native||{};
  var _ = elm.Native.Main||{};
  _.$op = {};
  _.main = main_0
  return elm.Main = _;
  };
  </script>"""
        render = "".join(render.split())
        self.assertEqual("".join(template.render(self._get_request_context()).strip().split()),render.strip())

if __name__ == '__main__':
    main()

