""" 定义函数 """

'''
auth:tangxje
time:20230404

'''

""" 练习1，定义1个函数 """
# def func_test1():  # 定义1个函数
#     print("*" * 50)
#
# def func_test2():  # 定义1个函数
#     func_test1()
#     print("hello")
#     func_test1()
# func_test2()

""" 练习2，定义形参mychar """
# def func_test11(mychar):  # 定义形参mychar
#     print(mychar * 50)
#
# def func_test22():
#     func_test11("#")
#     print("hello")
#     func_test11("*")
# func_test22()

"""练习3，定义mychar形参, mytime形参 """
# def func_test111(mychar):  # 定义mychar形参, mytime表示次数
#     print(mychar * 5)
#
# def func_test222():
#     func_test111("#" * 10)
#     print("hello")
#     func_test111("*" * 20)
#
# func_test222()

"""练习4, 输入个人信息：姓名、年龄、住址，把用户信息保存字典；封装用户信息函数 print_user_info，在函数中遍历字典中的键和值，并打印 """

# 方法一
# user_name = input("姓名：")
# user_age = input("年龄：")
# user_address = input("地址：")
# user_info = {
#     "name": user_name,
#     "age": user_age,
#     "address": user_address
# }  # 1、定义字典信息保存
#
# def print_user_info(userinfo):  # 2、封装函数
#     for key in userinfo:
#         print(key + ":" + userinfo[key])  # 根据键取值
#
# print_user_info(user_info)  # 3、打印

# # 方法二
# def print_user_info(user_info):
#     for key, value in user_info.items():
#         print('{}: {}'.format(key, value))
# user_info = {}
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
# address = input("请输入您的住址：")
#
# user_info['姓名'] = name
# user_info['年龄'] = age
# user_info['住址'] = address
#
# print_user_info(user_info)

""" 练习5 打印5行，每行打印10个字符串i love you """
# def put_line(lines, char, times):  # 定义形参(lines行数, char字符串, times次数)，下面用到
#     for i in range(1, lines + 1):
#         print(char * times)
# put_line(5, 'i love you,', 10)  # 打印5行，每行打印10个

""" 练习6 求阶乘的函数 例如所要求的数是5，则阶乘式是1*2*3*4*5，得到的积是120，所以120就是5的阶乘。"""
# n = int(input("输入正整数："))
# def jiechen(n):  # 方法一
#     if n == 1:
#         return 1
#     else:
#         return n * jiechen(n - 1)  # 递归调用自己
# print('{}的阶乘是{}'.format(n, jiechen(n)))  # {}表示格式化对应输出

# def jiechen(n):  # 方法二
#     n = int(input("输入正整数"))
#     count = 1
#     for i in range(1, n + 1):
#         count += 1
#         print(count)
# print(jiechen(n))  # 打印阶乘数

""" 函数总结：1、无参数无返回值 2、无参数有返回值 3、有参数无返回值 4、有参数有返回值 """

# def no_args_no_return_value():  # 1、无参数无返回值
#     print("直接打印其他，无关函数体")
# no_args_no_return_value()  # 结果为：直接打印其他，无关函数体
#
# def no_args_return_value():  # 2、无参数有返回值
#     year = int(input("输入年份:"))
#     return year
# print("无参数有返回值:", no_args_return_value())  # 结果为：无参数有返回值: 2023
#
# def have_args_no_return_value(name):  # 3、有参数无返回值
#     print("Welcome, " + name)  # 有name参数，也不显示数据
# have_args_no_return_value("lisa")  # 结果为：Welcome, lisa

""" 定义函数，函数外定义变量接收处理 """
# def func_name():
#     str1 = input("输入温度：")
#     str2 = input("输入湿度：")
#     str3 = input("输入高度：")
#     str4 = input("输入宽度：")
#     return str1, str2, str3, str4
# # print(func_name())  # 方法1：直接打印
# a, b, c, d = func_name()  # 方法2：定义4个变量，来接受数值
# print(a, b, c, d)

""" 函数，可变参数和不可变参数 """
# def add_numbers(num1, num2):  # 在函数内部，num1和num2是不可变的，所以无法通过函数修改a和b的值，只能在函数外部修改它们的值。
#     result = num1 + num2
#     print(result)
#     return result  # 不可变参数在函数内部无法被修改
#
# a = 10
# b = 20
# print(add_numbers(a, b))  # 输出结果为30

# def sum_numbers(*numbers):  # 1个*语法来表示接收任意个数的参数，并将它们放在一个元组中。2个**表示字典
#     result = 0
#     for num in numbers:  # for循环来遍历元组中的每个参数,并依次将它们相加。因为numbers是一个可变参数，所以可通过函数来修改它的值。
#         result += num
#     return result
# print(sum_numbers(1, 2, 3))  # 输出结果为6
# print(sum_numbers(1, 2, 3, 4, 5))  # 输出结果为15

""" 函数，可变参数，多值参数 """
# def demo(num, *args, **kwargs):  # *args表示元组，**kwargs表示字典
#     print(num)  # 结果为：1
#     print(args)  # 结果为： (2, 3, 4, 5)
#     print(kwargs)  # 结果为：{'name': '小明', 'age': 18, 'genter': True, 'high': 1.75}
# demo(1, 2, 3, 4, 5, name="小明", age=18, genter=True, high=1.75)
""" 函数，可变参数，求和计算 """
# def sum_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(sum_numbers(1, 2, 3))  # 结果为：6

""" 函数，可变参数，自动组成特定类型 """
# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# tuple1 = (1, 2, 3, 4, 5)
# dict1 = {"name": "zhangsan", "name2": "xiaoming"}
# demo(tuple1, dict1)

""" 函数，参数默认值,末尾格式 """
# def func_array_set_default_value(name, age, sex="男"):
#     print(name, age, sex)  # 结果为：zhangsan 18 男
#     # pass  # 空关键词，占位用的，暂时什么都不做的意思
# func_array_set_default_value("zhangsan", 18)

""" 函数，全局变量和局部变量 """
# result_outer = 100  # 全局变量
# def global_func():
#     result_inner = 10
#     print(result_inner)  # 局部变量，函数体内找到并打印。优先函数体内寻找
#     print(result_outer)  # 全局变量，函数体外找到并打印。
# global_func()

""" 函数，局部变量强制转换为全局变量 """
# a = 100  # 定义全局变量
#
# def global_func1():
#     global a  # 函数体内，定义全局变量参数
#     a = 1000  # 局部变量，传递到下一函数
#     print("func1的a值", a)  # 局部变量，函数体内找到并打印。优先函数体内寻找。 # 结果为 1000
# global_func1()

# def global_func2():
#     print("func2的a值", a)  # 结果为 1000
# global_func2()

""" 数组求和计算 """
lst = [1, 2, 3, 4, 5]
avg = sum(lst) - len(lst)
print(avg)
