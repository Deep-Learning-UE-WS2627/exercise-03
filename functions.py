def func1(a, b):

  if type(a) == int and type(b) == int:
    return a+b
  if type(a) == str and type(b) == str:
    return b+" "+a
  if a is None and b is None:
    return "Does not exist."
  if type(a) != type(b):
    return None
  return type(a)

def func2(*args):
  numberOfArgs = len(args)

  if numberOfArgs < 2:
    return str(numberOfArgs)
  if numberOfArgs == 2:
    return func1(a=args[0], b=args[1]) #der Return wurde hier dran gehangen, 
    #dass, wenn man den Funktionsaufruf von außen printen will, 
    #man ein vernünftiges Ergebnis zu sehen bekommt
    
  if numberOfArgs > 2:
    return numberOfArgs

def func3(**args):
  a_b_list = [args[key] for key in args if key=="a" or key=="b"]
  if len(a_b_list) == 2:
    #print("Test bestanden!")
    return func1(a=a_b_list[0], b=a_b_list[1])
  else:
    #print("Test verKACKT!")
    func2(args)

  
#print(func1(1,2))
#print(func1("Welt", "Hallo"))
#print(func1(None, None))
#print(func1(11, "Freunde"))
#print(func1(5.4, 3.6))

#print("Endergebnis:", func2(1,2))
#print("Anzahl der Argumente:", func2(3,4,2,2))
#print("Anzahl der Argumente: " + func2(1))

print(func3(b=1, a=3, c=1))
print(func3(a="a", b="v"))
print(func3(a=1))
print(func3(c=3, d="2"))