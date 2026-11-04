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
    case 2:
      func1(args[0], args[1])
    case x if x > 2 :
      return len(args)

def func3(*args2):
  if len(args2) == 2 & locals(args2[0]["__name__"]=="a") & locals(args2[1]["__name__"] == "b") :
    func1(args2[0], args2[1])
  else :
    func2(*args2)




func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)