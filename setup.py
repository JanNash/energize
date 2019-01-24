from re import findall
from setuptools import setup


meta_file = open("energize/metadata.py").read()
metadata = dict(findall("__([a-z]+)__\s*=\s*'([^']+)'", meta_file))


setup(
    name=metadata['packagename'],
    version=metadata['version'],
    description=metadata['description'],
    url=metadata['url'],
    author=metadata['author'],
    author_email=metadata['authoremail'],
    license=metadata['license'],
    packages=[metadata['packagename']],
    zip_safe=False
)
