#!/usr/bin/env python

from distutils.core import setup

setup(
    name='abyres.quotebuilder',
    version='0.1',
    description='Web frontend for Kinmu',
    author='Izhar Firdaus',
    author_email='kagesenshi.87@gmail.com',
    url='http://abyres.net/',
    package_dir={'':'src'},
    packages=['abyres', 'abyres.quotebuilder'],
    license='AGPLv3+',
    install_requires=[
        'morepath',
        'PyJWT==0.3.1',
        'pymongo',
        'DateTime',
        'kinmu.libs',
        'more.static',
        'more.chameleon',
        'werkzeug',
        'webtest',
    ],
    entry_points={
        'console_scripts' : [
            'frontend-start=kinmu.web.main:run'
        ]
    }

)
