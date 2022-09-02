

def type_logger(func):

  def val(x):    
    
    # res = func(x)
     print(f"{func.__name__}({(x)}: {type(x)})")
     print(f"{func.__name__}: {type(func)}")

 
  return val


@type_logger
def calc_cube(x):
   return x ** 3


calc_cube(8)

