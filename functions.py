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

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)


def func2(*args):
  n = len(args)
  if n < 2:
    return str(n)
  elif n==2:
    return func1(args[0], args[1])
  else:
   return n
  
  
print(func2())
print(func2(10))
print(func2(1,2))
print(func2(1,2,3))


def func3(**kwargs):
  if 'a' in kwargs and 'b' in kwargs:
    return func1(kwargs['a'], kwargs['b'])
  else:
    return func2(*kwargs.keys())
  
  
print(func3(a=1, b=2))
print(func3(x=5, y=6))
print(func3(a=1, c=3, d=4))
print(func3())