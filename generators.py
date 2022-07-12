def my_generator():
    n = 0
    while True:
        n += 1
        yield n

def my_generator2():
    my_list = [1, 2, 3]
    for i in my_list:
        yield i*2

gen = my_generator2()

for i in gen:
    print(i)
