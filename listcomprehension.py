x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]
newlist = []

a_list = [x * 2 for x in x]
b_list = [x for x in x if x % 2 == 0]
odd_list = [x for x in x if x % 2 != 0]
odd_list2= [[True]*x for x in x if x % 2 != 0]
s_list = [x for x in y if x is True or x == "True"]
c_list = [x for x in y if x is True]
d_list = [x for x in y if isinstance(x, str)]
llist = [] 
for x in x:
    if x % 2 != 0:
        llist.append(x)
e_list = odd_list2

print(a_list)
print(b_list)
print(odd_list)
print(s_list)
print(c_list)
print(e_list)