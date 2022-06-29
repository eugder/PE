def lists2dictionary(lst1: list[str], lst2: list[str]) -> dict:
    d = {}
    for i in range(len(lst1)):
        d[lst1[i]] = lst2[i]

    return d

def merge(d1: dict, d2: dict) -> dict:
    d1.update(d2)
    d3 = {**d1, **d2}

    return d1

# print(merge({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}))
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500

print(sample_dict)