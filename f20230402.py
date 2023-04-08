people = [
    {"name": "Alice", "age": 25, "gender": "F"},
    {"name": "Bob", "age": 30, "gender": "M"},
    {"name": "Charlie", "age": 35, "gender": "M"},
    {"name": "David", "age": 40, "gender": "M"},
    {"name": "Ella", "age": 45, "gender": "F"},
]
min_age = 40  # 最小年龄
max_age = 40  # 最大年龄
result = []   # 符合条件的字典列表
for person in people:
    if min_age <= person["age"] <= max_age:
        result.append(person)
print(result)
