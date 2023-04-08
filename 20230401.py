# 名片管理系统

cards = []  # 名片列表


# 添加名片函数
def add_card():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    email = input("请输入邮箱：")
    card = {"name": name, "phone": phone, "email": email}
    cards.append(card)
    print("添加成功！")


# 查询名片函数
def search_card():
    name = input("请输入要查找的姓名：")
    for card in cards:
        if card["name"] == name:
            print(f"姓名：{card['name']}，电话：{card['phone']}，邮箱：{card['email']}")
            break
    else:
        print("没有找到该名片！")


# 修改名片函数
def edit_card():
    name = input("请输入要修改的姓名：")
    for card in cards:
        if card["name"] == name:
            phone = input("请输入电话：")
            email = input("请输入邮箱：")
            card["phone"] = phone
            card["email"] = email
            print("修改成功！")
            break
    else:
        print("没有找到该名片！")


# 删除名片函数
def delete_card():
    name = input("请输入要删除的姓名：")
    for card in cards:
        if card["name"] == name:
            cards.remove(card)
            print("删除成功！")
            break
    else:
        print("没有找到该名片！")


# 打印所有名片函数
def show_all_cards():
    for card in cards:
        print(f"姓名：{card['name']}，电话：{card['phone']}，邮箱：{card['email']}")
    if not cards:
        print("没有名片，请添加！")


# 主函数
def main():
    while True:
        print("=" * 30)
        print("欢迎使用名片管理系统")
        print("1. 添加名片")
        print("2. 查询名片")
        print("3. 修改名片")
        print("4. 删除名片")
        print("5. 显示所有名片")
        print("0. 退出系统")
        print("=" * 30)

        choice = input("请输入您的选择：")
        if choice == "1":
            add_card()
        elif choice == "2":
            search_card()
        elif choice == "3":
            edit_card()
        elif choice == "4":
            delete_card()
        elif choice == "5":
            show_all_cards()
        elif choice == "0":
            print("谢谢使用名片管理系统，再见！")
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == '__main__':
    main()
