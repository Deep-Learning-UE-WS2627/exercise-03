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

# Write a function `func2` that takes an arbitrary number of arguments. In the function, check the number of arguments. If there are less than two arguments, return a string with the number of arguments. If there are two arguments, pass them to `func1`. If there are more than two arguments, return the number of arguments as an int value.

def func2(*args):
    if len(args) < 2:
        return f"Number of arguments: {len(args)}"
    elif len(args) == 2:
        return func1(args[0], args[1])
    else:
        return len(args)

# Next, write a function `func3` that takes an arbitrary number of named arguments. Check that two of these arguments have the names `a` and `b`. If so, pass them into `func1`. If not, pass all names of the arguments into `func2`.

def func3(**kwargs):
    if 'a' in kwargs and 'b' in kwargs:
        return func1(kwargs['a'], kwargs['b'])
    else:
        return func2(*kwargs.keys())