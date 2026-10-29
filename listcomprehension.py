x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]
#Step 3:
#Liste 'a' mit allen Elementen aus x * 2
a = [x*2 for x in x]
print(a)
#Liste b mit allen geraden Elementen aus x
b = [x for x in x if x%2 == 0]
print(b)
#Liste c mit allen Elementen aus y == True
c = [y for y in y if y == True]
print(c)
#Liste d mit allen Strings aus y
d = [y for y in y if type(y) == str]
print(d)
#Liste/Matrix e für ungerade Elemente aus x = True 
e = [[True for x in range(x)] for x in x if x%2 != 0]
print(e)