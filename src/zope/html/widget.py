##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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
"""Widget implementations for rich-text fields.

"""
__docformat__ = "reStructuredText"

import zope.formlib

import zc.resourcelibrary


class CkeditorWidget(zope.formlib.widgets.TextAreaWidget):

    editorHeight = 400

    configurationPath = "/@@/zope_ckconfig.js"

    def __call__(self):
        zc.resourcelibrary.need("ckeditor")
        #
        # XXX The 'shortname' here needs some salt to ensure that
        # multiple widgets with the same trailing name are
        # distinguishable; some encoding of the full name seems
        # appropriate, or a per-request counter would also do nicely.
        #
        d = {
            "config": self.configurationPath,
            "name": self.name,
            "shortname": self.name.split('.', 1)[-1],
            "height": self.editorHeight,
            }
        textarea = super(CkeditorWidget, self).__call__()
        return textarea + (self.javascriptTemplate % d)

    javascriptTemplate = '''
<script type="text/javascript" language="JavaScript">
var CKeditor_%(shortname)s = new CKEDITOR.replace("%(name)s",
    {
        height: %(height)s,
        customConfig : "%(config)s",
    }
);
</script>
'''
