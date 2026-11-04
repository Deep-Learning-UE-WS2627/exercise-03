x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# A list called `a` that contains all elements of `x`, multiplied by 2.
a = [i * 2 for i in x]
print(a)

# A list called `b` that contains all even elements of `x`.
b = [i for i in x if i % 2 == 0]
print(b)

# A list called `c` that contains all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
c = [i for i in y if i]
print(c)

# A list called `d` that contains all string elements of `y`
d1 = [i for i in y if isinstance(i, str)]
d2 = [i for i in y if type(i) == str]
print(d1)
print(d2)

# A list called `e` that contains a list for each odd element of `x`. The number of list elements is given by the current number of `x`, and all inner list elements are `True`. Use I.e., the list `e` starts like this: `[[True], [True, True, True], [True, True, True, True, True], ...]`
e1 = [[True] * i for i in x if i % 2 != 0]
e2 = [[True for j in range(i)] for i in x if i % 2 != 0]
print(e1)
print(e2)