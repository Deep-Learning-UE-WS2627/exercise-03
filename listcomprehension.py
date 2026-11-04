x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# New lists for ex. 3
# Put what is supposed to happe with x at the first spot.
# The last x is the array itself, multiplicating x just creates an array containing x's values twice
a = [x*2 for x in x]
# print(a)

# gives out a warning but works nonetheless ?
b = [i for i in x if i % 2 == 0]
# print(b)

c = [v for v in y if v == True]
# print(c)

d = [w for w in y if type(w) == str]
# print(d)

# list for each odd element in x: 1 3 5 7 9, list length equal to value of element in x
# I think this works, though I have no clue why :), renamed x to n to avoid variable shadowing (?)
e = [ [True for i in range(n)] for n in x if n % 2 != 0]
print(e)