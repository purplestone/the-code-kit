#coding=utf-8
import re, sys, os

def cur_file_dir():

    #获取脚本路径

    path = sys.path[0]

    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径

    if os.path.isdir(path):

        return path

    elif os.path.isfile(path):

        return os.path.dirname(path)


def checkXMLchar(s):
    '''Check Character Range and del'''
    s = [i for i in s if ord(i) == 9 or ord(i) == 10 or ord(i) == 13 or ord(i) > 32 and ord(i) < 55295 or ord(i) > 57344 and ord(i) < 65533 or ord(i) > 65536 and ord(i) < 1114111]
    s = ''.join(s)
    return s

def encodeXMLtext(s):
    '''xml textNode Data'''
    s = s.replace('&', '&amp;')
    s = s.replace('>', '&gt;')
    s = s.replace('<', '&lt;')
    return s

def encodeXMLattr(s):
    '''xml attributeNode Data'''
    s = s.replace('&', '&amp;')
    s = s.replace('>', '&gt;')
    s = s.replace('<', '&lt;')
    s = s.replace('"', '&quot;')
    s = s.replace('\n', '&#10;')
    s = s.replace('\r', '&#13;')
    s = s.replace('\t', '&#9;')
    return s

def decodeXMLdata(s):
    s = s.replace('&amp;', '&')
    s = s.replace('&gt;', '>')
    s = s.replace('&lt;', '<')
    s = s.replace('&quot;', '"')
    aD = re.findall(r'&#(\d+);',s)
    for c in aD:
        s = s.replace('&#'+c+';',unichr(int(c)))
    aD = re.findall(r'&#x(\w+);',s)
    for c in aD:
        s = s.replace('&#x'+c+';',unichr(int(c,16)))
    return s

def var_dump(o,fn='print'):
    d = 'none'
    l = o
    rs = print_r(l,fn,f='* ')
    if str(type(o)) == "<type 'dict'>":
        d = 'dict'
        l = o
    elif str(type(o)) == "<type 'list'>" or str(type(o)) == "<type 'tuple'>" or str(type(o)) == "<type 'set'>":
        d = 'set'
    else:
        try:
            l = o.__dict__
            d = 'dict'
        except AttributeError:
            pass
        else:
            pass

    n = 0
    if d == 'dict':
        for i in l:
            if i == '__doc__':
                rs += print_r('......',fn,f='    |--['+i+']    ')
            else:
                rs += print_r(l[i],fn,f='    |--['+i+']    ')
    elif d == 'set':
        for i in l:
            rs += print_r(i,fn,f='    |--['+str(n)+']    ')
            n += 1
    return rs

def print_r(o,fn='print',f='',d=''):
    rs = '%s(%s)    %s%s'%(str(f),str(o),type(o),str(d))
    if fn == 'print':
        print rs
    else:
        rs = fn(rs)
    return rs+'\n'



def print_dir(o,fn='print'):
    rs = print_r(o,fn,f='* ')
    for i in dir(o):
        if i == '__doc__':
            rs += print_r('......',fn,f='    |--['+i+']    ')
        else:
            rs += print_r(getattr(o,i),fn,f='    |--['+i+']    ')
    return rs

