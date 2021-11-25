my_list1 = [1, 2, 3, 10, 20, 30]
my_list2 = [item + 1 for item in my_list1 if item > 10]
my_dict2 = {item: item + 1 for item in my_list1 if item > 10}
my_gen2 = (item + 1 for item in my_list1 if item > 10)

print(next(my_gen2))
print(next(my_gen2))

my_sum2 = sum(my_gen2)

print(my_list2)
print(my_dict2)
print(my_sum2)

my_list = [1, 2, 3, 4]


def get_item(my_list):
    for item in my_list:
        yield item


for i in get_item(my_list):
    print(i)





