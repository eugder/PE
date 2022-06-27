def fml_symbols(in_str: str) -> str:
    return in_str[0]+in_str[len(in_str)//2]+in_str[-1]

def three_mid(in_str: str) -> str:
    mid = len(in_str)//2
    return in_str[mid-1]+in_str[mid]+in_str[mid+1]

def str_in_str(str1: str, str2: str) -> str:
    mid = len(str1)//2
    return str1[:mid]+str2+str1[mid:]

def arrange_syms(s: str) -> str:
    res = ""  # v1
    for i in s:
        if i.islower():
            res = i + res
        else:
            res = res + i

    s2 = sorted(s, reverse=True) # v2
    res2 = "".join(s2)

    return res, res2

def count_str(s:str) -> list[tuple]:
    digits = letters = symbols = 0
    for i in s:
        if i.isdecimal(): digits += 1
        elif i.isalpha(): letters += 1
        else: symbols += 1
    return digits, letters, symbols

def occurrences_substring(str1: str, str2: str) -> int:
    str1 = str1.lower()
    str2 = str2.lower()
    return str1.count(str2)

def empty_strings(str_lst: list[str]) -> list[str]:
    res = []
    for i in str_lst:
        if (i != "") and (i is not None):
            res.append(i)
    return res

def alphabets_numbers(s: str) -> list[str]:
    words = s.split(" ")
    res = []
    for word in words:
        for j in range(len(word)-1):
            if word[j].isalpha() and word[j+1].isdecimal():
                res.append(word)
    return res

def special_symbols(s: str) -> str:
    import string
    for i in string.punctuation:
        s = s.replace(i, "#")
    return s


print(special_symbols("/*Jon is @developer & musician!!"))
