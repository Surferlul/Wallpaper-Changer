# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# This file is generated by wxPython's PI generator.  Do not edit by hand.
#
# The *.pyi files are used by PyCharm and other development tools to provide
# more information, such as PEP 484 type hints, than it is able to glean from
# introspection of extension types and methods.  They are not intended to be
# imported, executed or used for any other purpose other than providing info
# to the tools. If you don't use use a tool that makes use of .pyi files then
# you can safely ignore this file.
#
# See: https://www.python.org/dev/peps/pep-0484/
#      https://www.jetbrains.com/help/pycharm/2016.1/type-hinting-in-pycharm.html
#
# Copyright: (c) 2020 by Total Control Software
# License:   wxWindows License
#---------------------------------------------------------------------------


"""
Some simple XML classes for use with XRC.

For more advanced XML needs it would be better to use one of the XML packages
provided by Python.
"""
#-- begin-_xml --#

import wx
XML_NO_INDENTATION = 0
XML_ELEMENT_NODE = 0
XML_ATTRIBUTE_NODE = 0
XML_TEXT_NODE = 0
XML_CDATA_SECTION_NODE = 0
XML_ENTITY_REF_NODE = 0
XML_ENTITY_NODE = 0
XML_PI_NODE = 0
XML_COMMENT_NODE = 0
XML_DOCUMENT_NODE = 0
XML_DOCUMENT_TYPE_NODE = 0
XML_DOCUMENT_FRAG_NODE = 0
XML_NOTATION_NODE = 0
XML_HTML_DOCUMENT_NODE = 0
XMLDOC_NONE = 0
XMLDOC_KEEP_WHITESPACE_NODES = 0

class XmlNode(object):
    """
    XmlNode(parent, type, name, content=wx.EmptyString, attrs=None, next=None, lineNo=-1)
    XmlNode(type, name, content=wx.EmptyString, lineNo=-1)
    XmlNode(node)
    
    Represents a node in an XML document.
    """

    def __init__(self, *args, **kw):
        """
        XmlNode(parent, type, name, content=wx.EmptyString, attrs=None, next=None, lineNo=-1)
        XmlNode(type, name, content=wx.EmptyString, lineNo=-1)
        XmlNode(node)
        
        Represents a node in an XML document.
        """

    def AddAttribute(self, *args, **kw):
        """
        AddAttribute(name, value)
        AddAttribute(attr)
        
        Appends a attribute with given name and value to the list of
        attributes for this node.
        """

    def AddChild(self, child):
        """
        AddChild(child)
        
        Adds node child as the last child of this node.
        """

    def DeleteAttribute(self, name):
        """
        DeleteAttribute(name) -> bool
        
        Removes the first attributes which has the given name from the list of
        attributes for this node.
        """

    def GetAttribute(self, attrName, defaultVal=wx.EmptyString):
        """
        GetAttribute(attrName, defaultVal=wx.EmptyString) -> String
        
        Returns the value of the attribute named attrName if it does exist.
        """

    def GetAttributes(self):
        """
        GetAttributes() -> XmlAttribute
        
        Return a pointer to the first attribute of this node.
        """

    def GetChildren(self):
        """
        GetChildren() -> XmlNode
        
        Returns the first child of this node.
        """

    def GetContent(self):
        """
        GetContent() -> String
        
        Returns the content of this node.
        """

    def GetDepth(self, grandparent=None):
        """
        GetDepth(grandparent=None) -> int
        
        Returns the number of nodes which separate this node from grandparent.
        """

    def GetNoConversion(self):
        """
        GetNoConversion() -> bool
        
        Returns a flag indicating whether encoding conversion is necessary
        when saving.
        """

    def GetLineNumber(self):
        """
        GetLineNumber() -> int
        
        Returns line number of the node in the input XML file or -1 if it is
        unknown.
        """

    def GetName(self):
        """
        GetName() -> String
        
        Returns the name of this node.
        """

    def GetNext(self):
        """
        GetNext() -> XmlNode
        
        Returns a pointer to the sibling of this node or NULL if there are no
        siblings.
        """

    def GetNodeContent(self):
        """
        GetNodeContent() -> String
        
        Returns the content of the first child node of type wxXML_TEXT_NODE or
        wxXML_CDATA_SECTION_NODE.
        """

    def GetParent(self):
        """
        GetParent() -> XmlNode
        
        Returns a pointer to the parent of this node or NULL if this node has
        no parent.
        """

    def GetType(self):
        """
        GetType() -> XmlNodeType
        
        Returns the type of this node.
        """

    def HasAttribute(self, attrName):
        """
        HasAttribute(attrName) -> bool
        
        Returns true if this node has a attribute named attrName.
        """

    def InsertChild(self, child, followingNode):
        """
        InsertChild(child, followingNode) -> bool
        
        Inserts the child node immediately before followingNode in the
        children list.
        """

    def InsertChildAfter(self, child, precedingNode):
        """
        InsertChildAfter(child, precedingNode) -> bool
        
        Inserts the child node immediately after precedingNode in the children
        list.
        """

    def IsWhitespaceOnly(self):
        """
        IsWhitespaceOnly() -> bool
        
        Returns true if the content of this node is a string containing only
        whitespaces (spaces, tabs, new lines, etc).
        """

    def RemoveChild(self, child):
        """
        RemoveChild(child) -> bool
        
        Removes the given node from the children list.
        """

    def SetContent(self, con):
        """
        SetContent(con)
        
        Sets the content of this node.
        """

    def SetName(self, name):
        """
        SetName(name)
        
        Sets the name of this node.
        """

    def SetNext(self, next):
        """
        SetNext(next)
        
        Sets as sibling the given node.
        """

    def SetNoConversion(self, noconversion):
        """
        SetNoConversion(noconversion)
        
        Sets a flag to indicate whether encoding conversion is necessary when
        saving.
        """

    def SetParent(self, parent):
        """
        SetParent(parent)
        
        Sets as parent the given node.
        """

    def SetType(self, type):
        """
        SetType(type)
        
        Sets the type of this node.
        """
    Attributes = property(None, None)
    Children = property(None, None)
    Content = property(None, None)
    Depth = property(None, None)
    LineNumber = property(None, None)
    Name = property(None, None)
    Next = property(None, None)
    NoConversion = property(None, None)
    NodeContent = property(None, None)
    Parent = property(None, None)
    Type = property(None, None)
# end of class XmlNode


class XmlAttribute(object):
    """
    XmlAttribute()
    XmlAttribute(name, value, next=None)
    
    Represents a node attribute.
    """

    def __init__(self, *args, **kw):
        """
        XmlAttribute()
        XmlAttribute(name, value, next=None)
        
        Represents a node attribute.
        """

    def GetName(self):
        """
        GetName() -> String
        
        Returns the name of this attribute.
        """

    def GetNext(self):
        """
        GetNext() -> XmlAttribute
        
        Returns the sibling of this attribute or NULL if there are no
        siblings.
        """

    def GetValue(self):
        """
        GetValue() -> String
        
        Returns the value of this attribute.
        """

    def SetName(self, name):
        """
        SetName(name)
        
        Sets the name of this attribute.
        """

    def SetNext(self, next):
        """
        SetNext(next)
        
        Sets the sibling of this attribute.
        """

    def SetValue(self, value):
        """
        SetValue(value)
        
        Sets the value of this attribute.
        """
    Name = property(None, None)
    Next = property(None, None)
    Value = property(None, None)
# end of class XmlAttribute


class XmlDocument(wx.Object):
    """
    XmlDocument()
    XmlDocument(doc)
    XmlDocument(filename, encoding="UTF-8")
    XmlDocument(stream, encoding="UTF-8")
    
    This class holds XML data/document as parsed by XML parser in the root
    node.
    """

    def __init__(self, *args, **kw):
        """
        XmlDocument()
        XmlDocument(doc)
        XmlDocument(filename, encoding="UTF-8")
        XmlDocument(stream, encoding="UTF-8")
        
        This class holds XML data/document as parsed by XML parser in the root
        node.
        """

    def AppendToProlog(self, node):
        """
        AppendToProlog(node)
        
        Appends a Process Instruction or Comment node to the document
        prologue.
        """

    def DetachDocumentNode(self):
        """
        DetachDocumentNode() -> XmlNode
        
        Detaches the document node and returns it.
        """

    def DetachRoot(self):
        """
        DetachRoot() -> XmlNode
        
        Detaches the root entity node and returns it.
        """

    def GetFileEncoding(self):
        """
        GetFileEncoding() -> String
        
        Returns encoding of document (may be empty).
        """

    def GetDoctype(self):
        """
        GetDoctype() -> XmlDoctype
        
        Returns the DOCTYPE declaration data for the document.
        """

    def GetFileType(self):
        """
        GetFileType() -> TextFileType
        
        Returns the output line ending format used for documents.
        """

    def GetEOL(self):
        """
        GetEOL() -> String
        
        Returns the output line ending string used for documents.
        """

    def GetDocumentNode(self):
        """
        GetDocumentNode() -> XmlNode
        
        Returns the document node of the document.
        """

    def GetRoot(self):
        """
        GetRoot() -> XmlNode
        
        Returns the root element node of the document.
        """

    def GetVersion(self):
        """
        GetVersion() -> String
        
        Returns the version of document.
        """

    def IsOk(self):
        """
        IsOk() -> bool
        
        Returns true if the document has been loaded successfully.
        """

    def Load(self, *args, **kw):
        """
        Load(filename, encoding="UTF-8", flags=XMLDOC_NONE) -> bool
        Load(stream, encoding="UTF-8", flags=XMLDOC_NONE) -> bool
        
        Parses filename as an xml document and loads its data.
        """

    def Save(self, *args, **kw):
        """
        Save(filename, indentstep=2) -> bool
        Save(stream, indentstep=2) -> bool
        
        Saves XML tree creating a file named with given string.
        """

    def SetDocumentNode(self, node):
        """
        SetDocumentNode(node)
        
        Sets the document node of this document.
        """

    def SetFileEncoding(self, encoding):
        """
        SetFileEncoding(encoding)
        
        Sets the encoding of the file which will be used to save the document.
        """

    def SetDoctype(self, doctype):
        """
        SetDoctype(doctype)
        
        Sets the data which will appear in the DOCTYPE declaration when the
        document is saved.
        """

    def SetFileType(self, fileType):
        """
        SetFileType(fileType)
        
        Sets the output line ending formats when the document is saved.
        """

    def SetRoot(self, node):
        """
        SetRoot(node)
        
        Sets the root element node of this document.
        """

    def SetVersion(self, version):
        """
        SetVersion(version)
        
        Sets the version of the XML file which will be used to save the
        document.
        """

    @staticmethod
    def GetLibraryVersionInfo():
        """
        GetLibraryVersionInfo() -> VersionInfo
        
        Get expat library version information.
        """
    Doctype = property(None, None)
    DocumentNode = property(None, None)
    EOL = property(None, None)
    FileEncoding = property(None, None)
    FileType = property(None, None)
    Root = property(None, None)
    Version = property(None, None)
# end of class XmlDocument


class XmlDoctype(object):
    """
    XmlDoctype(name="", sysid="", pubid="")
    
    Represents a DOCTYPE Declaration.
    """

    def __init__(self, name="", sysid="", pubid=""):
        """
        XmlDoctype(name="", sysid="", pubid="")
        
        Represents a DOCTYPE Declaration.
        """

    def Clear(self):
        """
        Clear()
        
        Removes all the DOCTYPE values.
        """

    def GetRootName(self):
        """
        GetRootName() -> String
        
        Returns the root name of the document.
        """

    def GetSystemId(self):
        """
        GetSystemId() -> String
        
        Returns the system id of the document.
        """

    def GetPublicId(self):
        """
        GetPublicId() -> String
        
        Returns the public id of the document.
        """

    def GetFullString(self):
        """
        GetFullString() -> String
        
        Returns the formatted DOCTYPE contents.
        """

    def IsValid(self):
        """
        IsValid() -> bool
        
        Returns true if the contents can produce a valid DOCTYPE string.
        """
    FullString = property(None, None)
    PublicId = property(None, None)
    RootName = property(None, None)
    SystemId = property(None, None)
# end of class XmlDoctype


XmlProperty = wx.deprecated(XmlAttribute, 'Use XmlProperty instead.')
#-- end-_xml --#
