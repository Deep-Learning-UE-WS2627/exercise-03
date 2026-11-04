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
  num_args = len(args)
  if num_args  < 2: 
    return str(num_args) 
  elif num_args == 2: 
    return func1(args[0], args[1])
  else:
    return num_args

def func3(**data):
    if 'a' in data and 'b' in data:
      return func2(data['a'], data['b'])
    else:
      return func3(*data.keys())

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

vgD  = [
  (1,2),                             
  ("Welt", "Hallo"),
  (None, None),
  (11, "Freunde"),
  (5.4, 3.6)
]

for a, b in vgD:
  res1 = func1(a, b)
  print(f"Result 1: {res1}")
  res2 = func2(a, b)
  print(f"Result 2: {res2}")
  res3 = func3(a=a, b=b)
  print(f"Result 3: {res3}")                      

print(func1(1,2))
print(func1("Welt", "Hallo"))
print(func1(None, None))
print(func1(11, "Freunde"))
print(func1(5.4, 3.6))
