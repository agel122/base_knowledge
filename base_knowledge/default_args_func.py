# correct way:
def my_append1(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


# wrong way:
def my_append2(item, my_list=[]):
    my_list.append(item)
    return my_list


print(my_append1(22))
print(my_append1(33))
print(my_append2(44))
print(my_append2(55))

