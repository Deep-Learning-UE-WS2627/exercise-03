import inspect


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
  match len(args):
    case 0 | 1 :
     print("Number of Arguments:" + str(len(args)))
     return 0
    case 2:
      func1(args[0], args[1])
      return 0
    case x if x > 2 :
      return len(args)

def func3(*args2):
  #if len(args2) == 2 & locals(args2[0]["__name__"]=="a") & locals(args2[1]["__name__"] == "b") : # This does not work
   # func1(args2[0], args2[1])

  # shamelessly copied from Stackexchange, inspired by Tutorial on W3Schools
  # A Frame (Stack Frame) is n Python, when you call a function you create something called a stack frame.
  # This frame is basically just a table of all the variables that are local to your function.
  frame = inspect.currentframe()
  if frame is None or frame.f_back is None:
    return
  caller_locals = inspect.currentframe().f_back.f_locals
  if args2[0] == "a" and "a" in caller_locals:
    if args2[1] == "b" and "b" in caller_locals:
        func1(args2[0], args2[1])
  else :
    func2(*args2)




func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)