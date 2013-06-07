from unittest import main, TestCase

import os

os.environ['DJANGO_SETTINGS_MODULE'] = "django-elm.tests.django_settings"

class ElmCompileTestCase(TestCase):
    def elm_inline_test(self):
        template = Template("""
            {% load elm_compiler %}
            {% elminline %}
            main = plainText "Hello"
            {% endelminline %}""")
        render = """

def __name__ == '__main__':
    main()
