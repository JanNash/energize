from re import findall
from setuptools import setup, find_packages


__description__ = '''
A package to help you setting up new projects with a fitting environment.
You have an idea, get coding lickety split!
'''


meta_file = open("licketysplit/metadata.py").read()
metadata = dict(findall("__([a-z]+)__\s*=\s*'([^']+)'", meta_file))


setup(
    name=metadata['packagename'],
    version=metadata['version'],
    description=__description__,
    url=metadata['url'],
    author=metadata['author'],
    author_email=metadata['authoremail'],
    license=metadata['license'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts' : [ 'licketysplit=licketysplit:main' ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ]
)
