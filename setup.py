#!/usr/bin/env python
import os
import sys
from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)
elif sys.argv[-1] == 'readme':
    def dedent(text):
        return '\n'.join([line[4:] for line in text.splitlines()])

    def header(text, sym):
        return '%s\n%s\n' % (text, sym * len(text))

    with open('README.rst', 'w') as fp:
        import choice_enum
        fp.write('%s\n%s\n\n%s%s%s%s' % (
            header('choice_enum', '='),
            choice_enum.__doc__,
            header('ChoiceEnumeration', '-'),
            dedent(choice_enum.ChoiceEnumeration.__doc__),
            header('make_enum_class', '-'),
            dedent(choice_enum.make_enum_class.__doc__)
        ))
    sys.exit(0)

classifiers = '''\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
'''.splitlines()

with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='choice_enum',
    version="0.3.1",
    author='David Krauth',
    author_email='dakrauth@gmail.com',
    url='https://github.com/dakrauth/choice_enum',
    license='MIT',
    platforms=['any'],
    py_modules=['choice_enum'],
    description="Wrapper class for defining DRY, encapsulated choice options for CharFields.",
    classifiers=classifiers,
    install_requires=['six'],
    long_description=long_description
)
