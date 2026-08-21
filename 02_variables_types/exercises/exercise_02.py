# 02_variables_types/exercises/exercise_02.py

# Convert string to int
int_var = int("42")
print(f"type of int_var : {type(int_var)} and value is : {int_var}\n")

# Convert string to float
float_var = float("3.14")
print(f"type of float_var : {type(float_var)} and value is : {float_var}\n")

# Convert int to string
str_var = str(100)
print(f"type of str_var : {type(str_var)} and value is : {str_var}\n")

# Convert float to int (truncates decimal part)
float_to_int = int(3.99)
print(f"type of float_to_int : {type(float_to_int)} and value is : {float_to_int}\n")
# int() truncates — it removes the decimal part, not rounds