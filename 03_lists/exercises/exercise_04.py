# Exercise 3.4: Shallow Copy and Deep Copy
# Requirements:
# - Create nested list [[1, 2], [3, 4]]
# - Create shallow copy and deep copy
# - Modify inner element of shallow copy — show original also changed
# - Modify inner element of deep copy — show original unchanged

import copy

list_of_list = [[1, 2], [3, 4]]

shallow_copy = list_of_list.copy()
deep_copy = copy.deepcopy(list_of_list)

shallow_copy[0][0] = 99
print(f"list_of_list : {list_of_list} --- shallow_copy : {shallow_copy}")

deep_copy[1][1] = 55
print(f"list_of_list : {list_of_list} --- deep_copy : {deep_copy}")