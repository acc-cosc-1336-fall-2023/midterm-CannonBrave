global_variable = 1

def use_global():
  global global_variable
  print("Old value: ", global_variable)
  global_variable += 1
  print("New value: ",global_variable)