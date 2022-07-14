# my_list = [(lambda x : x*10)(x) for x in range(10) if x%2==0]
# print (my_list)

my_list = [1, 2, 3]
my_iterator = my_list.__iter__()
print(my_iterator.__next__())
print(my_iterator.__next__())