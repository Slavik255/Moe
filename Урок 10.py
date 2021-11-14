#1) def calorie_calculator(name, get_calorie, spend_calorie):
#       if get_calorie > spend_calorie:
#           msg = name + " getting fat "
#       else:
#           msg = name + " lose weignt "
#       return msg
#   person = [" Nekit ", 1900, 1200]
#   print(calorie_calculator(*person))
#   print(calorie_calculator(" Slava ", 2000, 1950))

#2) def some(*args):
#       result = 0
#       for a in args:
#           result += a
#       print(result)
#   some(3, 12)
#   some(1, 5, 6)