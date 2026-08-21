# 02_variables_types/exercises/exercise_01.py

# Creating variables of different types
int_var = 10
float_var = 3.14
str_var = "MR_Rabie"
bool_var = True
none_var = None

print(f"type of int_var : {type(int_var)} and id is : {id(int_var)}\n")
print(f"type of float_var : {type(float_var)} and id is : {id(float_var)}\n")
print(f"type of str_var : {type(str_var)} and id is : {id(str_var)}\n")
print(f"type of bool_var : {type(bool_var)} and id is : {id(bool_var)}\n")
print(f"type of none_var : {type(none_var)} and id is : {id(none_var)}\n")

# Rebinding x to different types
x = 15
print(f"type of x : {type(x)} and id is : {id(x)}\n")

x = "str_15"
print(f"type of x : {type(x)} and id is : {id(x)}\n")

x = [10, 15]
print(f"type of x : {type(x)} and id is : {id(x)}\n")