from setuptools import setup, find_packages


setup(
    name="django-elm",
    packages = find_packages(),
    package_data={'': ['bin/elmToJS.hs'],'': ['static/js/*']},
    version = "0.1",
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
