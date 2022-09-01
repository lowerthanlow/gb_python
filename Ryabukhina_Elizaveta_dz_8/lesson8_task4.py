def val_checker(func):
  
  def checker(func_):

    def val(x):
      
      if func(x):
        return func_(x)
        
      raise ValueError  

    return val    

  return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
     return x ** 3

print(calc_cube(10))
print(calc_cube(-10))