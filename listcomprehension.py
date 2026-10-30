x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [value * 2 for value in x]
b = [value for value in x if value % 2 == 0]
c = [value for value in y if value]
d = [value for value in y if isinstance(value, str)]
e = [[True for _ in range(value)] for value in x if value % 2 != 0]

