x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# doppelte von N in Liste X
a = [n * 2 for n in x]

# wenn der Quotient ohne Rest ist
b = [n for n in x if n%2 == 0 ]

# wenn der Wert True gegeben ist
c = [n for n in y if n == True]
# falls alle Booleans gezählt werden sollten
# c = [n for n in y if bool(n)]

# prüft ob Strings vorhanden sind
d = [n for n in y if type(n) == str]


# returns jeden ungraden Wert und dessen Menge als True 
e = [[True]*n for n in x if n%2 != 0]




print(a)
print(b)
print(c)
print(d)
print(e)