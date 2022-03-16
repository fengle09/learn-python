#!/usr/bin/python3

"""
编码：
Py3 源码文件以 UTF-8 编码, 所有字符串都是 unicode 字符串。
"""

"""
标识符：
1. 第一个字符必须是字母表中的字母或下划线_。
2. 标识符的其他的部分由字母、数字和下划线组成。
3. 标识符对大小写敏感。
在Python3中，可以用中文作为变量名，非ASCII标识符也是允许的。
"""

"""
python保留字
保留字即关键字，我们不能把它们用作任何标识符名称。python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字：
不懂的关键字：
None,as,assert,async,await
def,except,finally,global,lambda
nonlocal,raise,pass,yield,with

import keyword
print(keyword.kwlist)
"""

"""
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print("1")
    print("True")
else:
    print("2")
    print("False")

"""
"""
多行语句
python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠\来实现多行语句，例如：
a = 1
b = 2
c = 3
total = a + \
     b + \
     c
print(total)
在[],{},或()中的多选语句，不需要使用反斜杠\
"""

"""
数字（Number）类型
python中数字有四种类型：整数、布尔、浮点数和复数。
int（整数），如1，只有一种整数类型int，表示为长整型，没有python2中的Long.
bool（布尔），如：True
float（浮点数），如：1.23,3E-2
complex（复数），如：1+2j,1.1+2.2j
"""

"""
字符串（String）类型
python 中单引号’和双引号”使用完全相同。
使用三引号（‘’‘或“”“）可以指定一个多行字符串。
转义符\。
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
python中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
python中的字符串不能改变。
python没有单独的字符类型，一个字符就是他要1的字符串。
字符串的截取的语法格式如下：变量[头下标：尾下标：步长]
word = '字符串'
sentence = "这是一个句子"
paragraph = '''这是一个段落,
可以由多行组成'''
"""
"""
str='123456789'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str * 2)
print(str + '你好')
print('hello\nrunoob')
print(r'hello\nhaha')
这里的r指raw,即raw string，会自动将反斜杠转义，
"""
"""
等待用户输入
执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下 enter 键后退出")
同一行显示多条语句
python可以在同一行中使用多条语句，语句之间使用分号;分割，以下是一个简单的实例：
import sys; x = 'runoob';sys.stdout.write(x + '\n')
"""

"""
import与from...import
在python用import或from...import来导入相应的模块
将整个模块（somemodule）导入，格式为：import somemodule
从某个模块中导入某个函数，格式为：from somemodule import somefunction
从某个模块中导入多个函数，格式为：from somemodule import firstfunc,secondfunc,thirdfunc
将某个模块中的全部函数导入，格式为：from somemodule import *
导入sys模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

导入sys模块的argv,path成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

"""

"""
命令行参数
很多程序可以执行一些操作来查看一些基本信息，python可以使用-h参数查看各参数帮助信息。
"""


