from re import findall
from setuptools import setup


__description__ = '''
A package to help you setting up new projects with a fitting environment.
Just set a course, dramatically pause for a moment and 'energize' :).
'''


meta_file = open("energize/metadata.py").read()
metadata = dict(findall("__([a-z]+)__\s*=\s*'([^']+)'", meta_file))


setup(
    name=metadata['packagename'],
    version=metadata['version'],
    description=__description__,
    url=metadata['url'],
    author=metadata['author'],
    author_email=metadata['authoremail'],
    license=metadata['license'],
    packages=[metadata['packagename']],
    zip_safe=False,
    entry_points = {
        'console_scripts' : [ 'energize=energize:main' ],
    },
)
