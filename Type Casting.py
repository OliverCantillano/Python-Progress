# Typecasting = process of converting a variable from one data type to another
# str(), int(), float(), bool()  /// we use "type" to know the variable type

name = 'oliver'
age = 22
gpa = 3.5
is_student = True

type(is_student)
print(type(is_student))
# if we don't put the print(type(is_student)) then when we run it won't show anything

# /////

# Here can change the variable type by doing the following:
gpa = int(gpa)
print(gpa)
# We changed the gpa from a "float" type to "int", we can confirm since it has no decimals
age = float(age)
print(age)
# Here we did the opposite, we can confirm its correct because now age has decimals


# If we convert a "str" to a "bool" if the space has a value in it will show "true"
# But if the name value is empty it will show "false"
name = bool(name)
print(name)

# *Example irl
# Client needs to enter a value, if they don't it gives "false" and they are prompted back to enter value