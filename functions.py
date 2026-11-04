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
  numArgs = len(args)

  if numArgs < 2:
    return str(numArgs)

  if numArgs == 2:
    return func1(*args)
  
  return numArgs

def func3(**kwargs):
  if "a" in kwargs and "b" in kwargs:
    return func1(kwargs['a'], kwargs['b'])
  return func2(*kwargs)

print(
func1(1,2),
func1("Welt", "Hallo"),
func1(None, None),
func1(11, "Freunde"),
func1(5.4, 3.6),

func2(2, 3, 4),
func2("hallo"),
func2(None, 3, "test", 3.5),

func3(a=2, b=4, c=7, e='test'),
func3(a=2, c=3, d=None, e='test'),

sep="\n"
)
