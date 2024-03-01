import re


def replace_underscore(text, index, combinations, current):
    # 如果已经到达文本末尾，则将当前数字组合添加到列表中
    if index == len(text):
        combinations.append(current)
        return
    # 如果当前字符为下划线，则遍历数字0-9并递归地继续填充下一个位置
    if text[index] == '_':
        for i in range(10):
            replace_underscore(text, index + 1, combinations, current + str(i))
    # 如果当前字符不是下划线，则直接将当前字符添加到数字组合中并继续填充下一个位置
    else:
        replace_underscore(text, index + 1, combinations, current + text[index])


text = input("请输入要补全的数字，未知数字请用下划线代替：")

# 查找文本中是否包含下划线
match = re.findall(r"_", text)

# 如果文本中包含下划线，则进行数字补全
if match:
    print(f"下划线出现次数：{len(match)}")
    print("正在补全，请稍等……")

    # 创建一个空列表来存储所有可能的数字组合
    combinations = []
    # 使用 replace_underscore 函数递归地填充所有可能的数字组合
    replace_underscore(text, 0, combinations, "")

    print("补全后的数字组合：")
    # 遍历所有数字组合，并打印出来
    for combination in combinations:
        print(combination)
# 如果文本中不包含下划线，则打印提示信息
else:
    print("未找到下划线，请认真输入")
