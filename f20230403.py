import time

card_box = []  # 定义空的框子，用来存储名片数据

print("*" * 50)
print("欢迎使用【名片管理系统】v1.0")
print("1、新建名片")
print("2、显示名片")
print("3、查询名片")
print("0、退出系统")
print("*" * 50)

user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))

while True:
    if user_choice == 1:
        name = input("输入姓名：")
        phone = input("输入电话：")
        QQ = input("输入QQ：")
        mail = input("输入邮件：")
        card = {"name": name, "phone": phone, "QQ": QQ, "mail": mail}  # 纳入字典数据
        card_box.append(card)
        print("添加成功：", card_box, "", len(card_box))
        user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))

    elif user_choice == 2:
        if len(card_box) == 0:  # 显示所有名片
            print(card_box)
            user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))
        else:
            print('没有名片，请添加！')
            print(card_box)
            user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))

    elif user_choice == 3:
        card_query = []  # 先定义空框子，当查询到则塞入
        find_name = input('输入要查找的姓名：')
        for i in card_box:
            if i['name'] == find_name:  # 根据条件查询名片
                card_query.append(i)
                print(card_query)
                user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))
            else:
                print('没找到')

    elif user_choice == 0:
        print('退出系统')
        break

    else:
        print('选择错误,重新输入：')
        user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))
        if user_choice == 1:
            name = input("输入姓名：")
            phone = input("输入电话：")
            QQ = input("输入QQ：")
            mail = input("输入邮件：")
            card = {"name": name, "phone": phone, "QQ": QQ, "mail": mail}  # 纳入字典数据
            card_box.append(card)
            print("添加成功：", card_box)
            user_choice = int(input("请输入操作数字，1表示新建，2、表示显示，3表示查询，0退出系统："))
            time.sleep(5)
            print('超时5秒了，再见！')  # 等待5秒，超时就退出
    break
