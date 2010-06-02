##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.html package

$Id: setup.py 80818 2007-10-11 04:06:12Z srichter $
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='zope.html',
      version = '0',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='HTML and XHTML Editing Support',
      long_description=(
          read('README.txt')
          + '\n\n' +
          'Detailed Documentation\n' +
          '======================\n\n'
          + '\n\n' +
          read('src', 'zope', 'html', 'README.txt')
          + '\n\n' +
          read('src', 'zope', 'html', 'docinfo.txt')
          + '\n\n' +
          read('src', 'zope', 'html', 'widget.txt')
          + '\n\n' +
          read('src', 'zope', 'html', 'browser.txt')
          + '\n\n' +
          read('CHANGES.txt')
          ),
      keywords = "zope3 html widget fsck editor",
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      url='http://cheeseshop.python.org/pypi/zope.html',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope'],
      extras_require = dict(
          test=['zope.app.authentication',
                'zope.app.debugskin',
                'zope.app.server',
                'zope.app.testing',
                'zope.app.zcmlfiles',
                'zope.testing',
                'zope.testbrowser',
                ]),
      install_requires=[
          'pytz',
          'setuptools',
          'zc.resourcelibrary',
          'ZODB3',
          'zope.annotation',
          'zope.app.form',
          'zope.component',
          'zope.event',
          'zope.file',
          'zope.formlib',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.mimetype',
          'zope.publisher',
          'zope.schema',
          ],
      include_package_data = True,
      zip_safe = False,
      )
