"""1:"""
print('1:')


def string(str: str) -> bool:
    list_brackets: list[str] = []
    for i in str:
        if i in ['{', '[', '(']:
            list_brackets.append(i)
            continue
        if i in [']', '}', ')']:
            if len(list_brackets) == 0:
                return False
            end = list_brackets[-1]
            if i == '}' and end == '{' or i == ']' and \
                    end == '[' or i == ')' and end == '(':
                list_brackets.pop()
            else:
                return False
    if len(list_brackets) > 0:
        return False
    else:
        return True


print(string(input('enter a string:')))
print('2:')
"""2"""


def sorted_list(list_2: list[int]) -> None:
    index: int = 1
    while index < len(list_2):
        if list_2[index] == list_2[index - 1]:
            list_2.pop(index)
        else:
            index += 1


list_2: list[int] = [1, 1, 1, 2, 3, 4, 4, 5]
sorted_list(list_2)
print(list_2)

"""3"""
print('3:')


def list3(list1: list[int], list2: list[int]) -> list:
    new_list: list[int] = []
    while True:
        if len(list1) == 0:
            new_list.extend(list2)
            return new_list
        if len(list2) == 0:
            new_list.extend(list1)
            return new_list
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)


print(list3([1, 2, 3, 3, 3, 5], [1, 2, 2, 3, 4]))
