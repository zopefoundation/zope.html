"""Interfaces and fields for HTML/XHTML documents.

"""
__docformat__ = "reStructuredText"

import zope.interface
import zope.schema
import zope.schema.interfaces


class IHtmlTextField(zope.schema.interfaces.IText):
    """Text that contains HTML markup.

    This is an abstract interface.  Only the concrete derived
    interfaces should be used for actual field definitions.

    """


class IHtmlDocumentField(IHtmlTextField):
    """HTML document field.

    This is for fields that represent complete HTML documents,
    including the document head as well as the body.

    """


class IHtmlFragmentField(IHtmlTextField):
    """HTML fragment field.

    This is for fields that represent pieces of HTML that can be
    composed to create complete documents.  This field implies no
    specifics about what portion of an HTML document is represented,
    but it must be internally well-formed.

    """


class IXhtmlTextField(zope.schema.interfaces.IText):
    """Text that contains XHTML markup.

    This is an abstract interface.  Only the concrete derived
    interfaces should be used for actual field definitions.

    """


class IXhtmlDocumentField(IXhtmlTextField):
    """XHTML document field.

    This is for fields that represent complete XHTML documents,
    including the document head as well as the body.

    """


class IXhtmlFragmentField(IXhtmlTextField):
    """XHTML fragment field.

    This is for fields that represent pieces of XHTML that can be
    composed to create complete documents.  This field implies no
    specifics about what portion of an HTML document is represented,
    but it must be internally well-formed.

    """


class HtmlDocument(zope.schema.Text):

    zope.interface.implements(IHtmlDocumentField)


class HtmlFragment(zope.schema.Text):

    zope.interface.implements(IHtmlFragmentField)


class XhtmlDocument(zope.schema.Text):

    zope.interface.implements(IXhtmlDocumentField)


class XhtmlFragment(zope.schema.Text):

    zope.interface.implements(IXhtmlFragmentField)
