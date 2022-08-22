# my_list = [(lambda x : x*10)(x) for x in range(10) if x%2==0]
# print (my_list)

s = "a2b3c4"

res = ""
for i in range(0,len(s)-1,2):
    res += s[i]*int(s[i+1])
print(res, list(s))