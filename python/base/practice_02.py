import keyword
import sys

"""
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
    int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    bool (布尔), 如 True。
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j

字符串(String)
    python中单引号和双引号使用完全相同。
    反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    Python中的字符串不能改变。
    Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    字符串的截取的语法格式如下：变量[头下标:尾下标:步长] 笔记：下标从零开始，不包含尾下标。类似数学中[头下标,尾下标) 左闭区右开

Tuple（元组）
    元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
    例如：tuple = ( 'abcd', 123 , 2.23, 70.2  )
    注意：
        元组中只包含一个元素时，需要在元素后面添加逗号“,” ，否则括号会被当作运算符使用。
            例如：type((9527))--><class 'int'> ; type((9527)) --> <class 'tuple'>

Set（集合）
    集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
    基本功能是进行成员关系测试和删除重复元素。
    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
    创建格式：
        parame = {value01,value02,...}
        或者
        set(value)

Dictionary（字典）
    字典（dictionary）是Python中另一个非常有用的内置数据类型。
    列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
    键(key)必须使用不可变类型。
    在同一个字典中，键(key)必须是唯一的。

输出(print)
    默认输出是换行的，如果要实现不换行需要在变量末尾加上 end = ""


拓展：
    字典推导式
        语法一：
            key：字典中的key
            value：字典中的value
            dict.items()：序列
            condition：条件表达式
            key_exp：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp处理 
            value_exp：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp处理
            具体：{key_exp:value_exp for key,value in dict.items() if condition}
        语法二：
            key：字典中的key 
            value：字典中的value 
            dict.items()：序列 
            condition：条件表达式 
            key_exp：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp处理 
            value_exp1：在for循环中，如果条件表达式condition成立(即条件表达式成立)，返回对应的key,value并作key_exp,value_exp1处理
            value_exp2：在for循环中，如果条件表达式condition不成立(即条件表达式不成立)，返回对应的key,value并作key_exp,value_exp2处理
            具体：{key_exp:value_exp1 if condition else value_exp2 for key,value in dict.items()}

    range函数    
        语法：range(start, stop[, step]) 或 range(stop)
        参数说明：
            start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
            stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
            step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        注意：
            Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
                例如：range(0, 5, 1) 输出：<class 'range'>
            Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
                例如：range(0, 5, 1) 输出：[0, 1, 2, 3, 4]

"""

'''
# 输出所有python保留的关键字
keywords = keyword.kwlist
for temp_keyword in keywords:
    print(temp_keyword)
'''

'''
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。（这里的 r 指 raw，即 raw string，会自动将反斜杠转义）例如：
print("how are you?\nyes,I'm fine")
print(r"how are you?\nyes,I'm fine")
'''

'''
# 符串可以用 + 运算符连接在一起，用 * 运算符重复(字符串和整数)。
print("重要的事" + "说三遍：")
print("this is string\n" * 3)
'''

'''
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长] 笔记：下标从零开始，不包含尾下标。类似数学中[头下标,尾下标) 左闭区右开
str = '0123456789'
print(str[1:5:2])
# 步长可以为负数
print(str[5:1:-1])
# 下标可以未负数
print(str[-5:0:-1])
# 不填写尾标时，输出从头下标开始后的所有字符
print(str[1:])
# 逆向输出：第一个参数 -1 表示最后一个元素 第二个参数为空，表示移动到列表末尾 第三个参数为步长，-1 表示逆向
print(str[-1::-1])
'''

'''
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
# set集合会自动去重
print(a)
print(b)
# a 和 b 的差集
print(a - b)
# a 和 b 的并集
print(a | b)
# a 和 b 的交集
print(a & b)
# a 和 b 中不同时存在的元素
print(a ^ b)
'''

'''
# dict创建方法
dict1 = dict([('Baidu', 1), ('Ali', 2), ('Taobao', 3)])
print(dict1)
# 字典推导式
dict2 = {x: x ** 2 for x in range(2, 7, 2)}
print(dict2)
dict3 = dict(Baidu=1, Ali=2, Taobao=3)
print(dict3)
'''

'''
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()
'''

# 进制转换
'''
# 数字转二进制
print(bin(65))
# 数字转八进制
print(oct(65))
# 数字转十六进制
print(hex(65))
# 数字转字符
print(chr(65))
# 字符转数字
print(ord('B'))
'''

# 使用迭代器遍历 next最后一个元素会报StopIteration异常
'''
# _list = [3, 6, 5]  # 列表
# _list = ("一号玩家", "二号玩家", "十号玩家")  # 元组
_list = {"name": "姨太太", "age": 19, "sex": "女"}  # 字典
# _list = {8, '10', 5}  # 集合
it = iter(_list)
while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        # sys.exit()
        break     
'''
