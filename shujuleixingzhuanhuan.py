"""
python3 数据类型转换
python数据类型转换可以公为两种：
隐士类型转换-自动完成
显式类型转换-需要使用类型函数来转换
隐式类型转换
在隐式类型转换中，python会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。
a = 123
b = 1.23
c = a + b
print("datatype of a_int:", type(a))
print("datatype of a_flo:", type(b))

print("value of a_new:", c)
print("datatype of a_new:", type(c))

整数与字符串相加，不可以
num_int = 123
num_str = "456"
print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))
print(num_int+num_str)
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。
int() 强制转换为整型：
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3
x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'
整型和字符串类型进行运算，就可以用强制类型转换来完成：
num_int = 123
num_str = "456"
print("num_int 数据类型为:", type(num_int))
print("类型转换前，num_str 数据类型为:", type(num_str))
num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:", type(num_str))
num_sum = num_int + num_str
print("num_int 与 num_str 相加结果为:", num_sum)
print("sum 数据类型为:", type(num_sum))
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

函数	描述
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

