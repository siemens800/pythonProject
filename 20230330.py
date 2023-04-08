"""
Python取位数，写完整好记忆。草泥马简写，不好记。
12345 // 1 %10 #取个位，简写 12345 % 10
12345 // 10 %10 #取十位
12345 // 100 %10 #取百位
12345 // 1000 %10 #取千位
12345 // 10000 %10 #取万位，简写 12345 // 10000
"""

# tuple1 = ("zhangsan", 18, 1.75, "zhangsan")  # 定义元组
# print(tuple1[1])
# # tuple1[1] = 19  # 元组元素不能修改，所以报错

# print("根据值查询索引位置，返回首次出现时的索引，没有查到会报错", tuple1.index("zhangsan"))
# print("数据在元组中出现的次数：", tuple1.count("zhangsan"))  # 数据在元组中出现的次数
# print("打印元组的长度：", len(tuple1))  # 打印元组的长度
# for i in tuple1:
#     print(i)

# info = 10, 20  #
# print("打印数据类型，如元组 ：", type(info))

# a = 10
# b = 20
# a, b = b, a  # 先自动组包，再自动解包
# print(a, b)

# info = ("zhangsan", 18)
# print("%s 的年龄时 %d" % info)

# lst1 = [1, 2, 3, 4, 'a', 'asdfsdf']
# tuple1 = tuple(lst1)
# print("列表==元组，相互转化。列表转成元组数据：", type(tuple1), '\n', tuple1)

# tuple2 = tuple[1, 2, 3, 4, 'a', 'asdfsdf']  # 直接定义为：tuple元组数据
# lst2 = list(tuple2)  # 强转成 list数据
# print("列表==元组，相互转化。元组转成列表数据：", type(lst2), '\n', lst2)

# 定义一个字典
person = {
    "name": "zhangsan",
    "age": 18,
    "sex": "男",
    "high": 1.75
}
# print(person["name"])
# print(person)
#
# person["date"] = "2021-10-10"  # 字典尾部直接添加新数据
# print(person)
#
# del person["date"]  # del 字典[键], 直接删除数据
# print(person)

# a = person.pop("name")  # 删除指定键值对,返回被删除的值
# print(a)
# print(person)
#
# person.clear()  # 清空字典
# print(person)

# student = {
#     "name": "zhangsan",
#     "age": 19,
#     "sex": "女"
# }
# lst = [{"name": "zhangsan", "age": 19, "sex": "女"},
#        {"name": "lisi", "age": 19, "sex": "女"},
#        {"name": "wangwu", "age": 19, "sex": "女"},
#        {"name": "chenliu", "age": 19, "sex": "女"},
#        ]
# print(lst[0])  # 查询zhangsan的信息
# print(lst[0]["age"])  # 查询zhangsan的年龄 , 注意：字典无序排列，所以用age查询
# print(lst[1].keys())  # 查询lisi所有的属性定义
# print(lst[1].values())  # 查询lisi所有的存储数据

""" 
my_list = [
            {'id': 1,'money': 10}, {'id': 2, 'money': 20}, 
            {'id': 3, 'money': 30}, {'id': 4, 'money': 40}
           ]
要求: 编程：功能如下
    1. 如果字典中 ID 的值为奇数,则对 money 的值加 20
    2. 如果字典中 ID 的值为偶数, 则对 money 的值加 10
    3. 打印输出列表,查看最终的结果
"""
# my_dict = {'001': {'name': '小明', 'ID': 1, 'money': 100},
#            '002': {'name': '小红', 'ID': 2, 'money': 200},
#            '003': {'name': '小刚', 'ID': 3, 'money': 300},
#            '004': {'name': '小莉', 'ID': 4, 'money': 400}}
# for key, value in my_dict.items():
#     if value.get('ID') % 2 == 0:  # 取模，奇数
#         value['money'] += 10
#     else:
#         value['money'] += 20
# print(my_dict)

""" 
my_list = [
            {'id': 1,'money': 10}, {'id': 2, 'money': 20}, 
            {'id': 3, 'money': 30}, {'id': 4, 'money': 40}
           ]
要求: 编程：功能如下
    1. 如果字典中 ID 的值为奇数,则对 money 的值加 20
    2. 如果字典中 ID 的值为偶数, 则对 money 的值加 10
    3. 打印输出列表,查看最终的结果
"""
# my_lst = [{'id': 1, 'money': 10}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
# for i in my_lst:
#     if i.get("id") % 2 == 0:  # 取模，偶数
#         i['money'] = i['money'] + 10
#     else:
#         i['money'] = i['money'] + 20
# print(my_lst)

