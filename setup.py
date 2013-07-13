from setuptools import setup, find_packages

import subprocess


def compile_hs_file(filename):
    subprocess.call("ghc "+filename ,shell=True)

compile_hs_file("elm/bin/elmToJS.hs")

setup(
    name="django-elm",
    packages = find_packages(),
    package_data={'elm': ['bin/elmToJS'],'': ['static/js/*']},
    version = "0.1.2",
    author = "Joel Hermanns",
    author_email = "joel.hermanns@gmail.com",
    url = "",
    description = "Django template tags to compile Elm to Javascript",
    classifiers = [
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ["elm"],
)
