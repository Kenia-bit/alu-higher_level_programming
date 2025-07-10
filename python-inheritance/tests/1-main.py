#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print("Original list:", my_list)
sorted_version = my_list.print_sorted()
print("Returned sorted list:", sorted_version)
print("Original list after sorting:", my_list)
