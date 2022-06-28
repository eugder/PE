def reverse_list (l:list) -> list:
    l.reverse()
    print (l)

def concatenate_two(list1: list[str], list2: list[str]) -> list[str]:
    size = min(len(list1), len(list2))
    result = []
    for i in range(size):
        result.append(list1[i] + list2[i])
    if len(list1) > len(list2):
        result = result + list1[size:]
    elif len(list2) > len(list1):
        result = result + list2[size:]

    return result

def items2square(l: list[int]) -> list[int]:
    for i in range(len(l)):
        l[i] = l[i]*l[i]
    return l

def Iterate_both(lst1: list[int], lst2: list[int]):
    lst2.reverse()
    print(lst2)
    for i in range(len(lst1)):
        print("{0} {1}".format(lst1[i], lst2[i]))



print (Iterate_both([10, 20, 30, 40], [100, 200, 300, 400]))