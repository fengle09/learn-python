"""
Python3 基本数据类型
python中的变量不需要声明。每个变量在使用前都必须赋值。变量赋值以后该变量才会被创建。
在python中，变量就是变量，它没有类型，我们所说的“类型”是变量所指的内存中对象的类型。
"""

"""
标准数据类型
python中有六个标准的数据类型：
Number(数字),String(字符串),List(列表),Tuple(元组),Set(集合),Dictionary(字典)
Python3的六个标准数据类型中：
不可变数据（3个）：Number(数字),String(字符串),Tuple(元组)
可变数据（3个）：List(列表),Set(集合),Dictionary(字典)
"""

"""
Number(数字)
python3支持int,float,bool,complex(复数)
在python3里，只有一种整数类型int，表示为长整形，没有python2中的Long.
像大多数语言一样，数值类型的复制和计算都是很直观的。
内置的type()函数可以用来查询变量所指的对象类型。
a, b, c, d =20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a = 111
ret = isinstance(a, int)
print(ret)

isinstance 和type的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)

print(isinstance(B(), A))
print(type(B()) == A)
print(issubclass(B, A))

1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
a = 2
print(a ** 10)

str = 'Runoob'
str = 'aaaaaa'

print(str)          # 输出字符串
print(str[-4:4])
print(str[2:-2])

"""

"""
List(列表)
List是python中使用最频繁的数据类型
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字、字符串甚至可以包含列表（所谓嵌套）
列表是写在方括号[]之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]
索引值以0为开始值，-1为从末尾的开始位置。
+表示连接运算符，星号*表示重复操作。如下实例：
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
python列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引1到索引4的位置并设置为步长为2（间隔一个位置）来截取字条串：
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list[1:4:2])

def reverseWords(input):
    inputWords = input.split(" ")
    print(inputWords)
    inputWords = inputWords[-1::-1]
    print(inputWords)
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = 'I like runoob a'
    rw = reverseWords(input)
    print(rw)
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

string、list 和 tuple 都属于 sequence（序列）
注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
4、元组也可以使用+操作符进行拼接。
"""
"""
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)

----------------------------
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')
a = set('abc')
b = set('bcd')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
"""

"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values()) # 输出所有值

注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。

int(x [,base]),将x转换为一个整数

float(x),将x转换到一个浮点数

complex(real [,imag]),创建一个复数

str(x),将对象 x 转换为字符串

repr(x),将对象 x 转换为表达式字符串

eval(str),用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s),将序列 s 转换为一个元组

list(s),将序列 s 转换为一个列表

set(s),转换为可变集合

dict(d),创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s),转换为不可变集合

chr(x),将一个整数转换为一个字符

ord(x),将一个字符转换为它的整数值

hex(x),将一个整数转换为一个十六进制字符串

oct(x),将一个整数转换为一个八进制字符串
"""





