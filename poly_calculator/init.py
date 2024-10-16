from opeartions import add, sub, mult, div, exp, poly_deriv
from colorama import Fore, Back, Style, init
import keyboard

"""
   Initialization function menu 
"""
def main_options() -> None:
   
   init() #Initialize colorama
   
   print("---------------------------")
   print("WELCOME TO POLY CALCULATOR")
   print("---------------------------")
   print("Press Q key to quit")
   print()
   
   while True:
      options = ("1 - Addition", "2 - Subtraction", "3 - Division", "4 - Multiplication", "5 - Exponential", "0 - Advanced Operations")
      print("Please select an operation:")
      print(options)
      selected_option = int(input())
      
      # if keyboard.read_key() == "q":
      #       break
      
      if selected_option in (1, 2, 3, 4, 5):
         try:
            
            values = input("Now set both numbers separated by a space (x y): ")
            if len(values.split(" ")) != 2:
               raise ValueError

            input_values = values.split(" ")
            x = float(input_values[0])
            y = float(input_values[1])
            
         except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number")
            continue
         
         finally:
            print(Style.RESET_ALL)
         
         basic_calcs(selected_option, x, y)
      
      elif selected_option == 0:
         options_advanced = ("1 - Derivative", "2 - Integration")
         print(options_advanced)
         selected_option = int(input())
         if selected_option in (1, 2):
            try:
               values = input("Set f(x) = ")
               
            except ValueError:
               print(Fore.RED + "Invalid input. Please enter a number")
               continue
            
            finally:
               print(Style.RESET_ALL)
         
         advanced_calcs(selected_option, values)
         
      else:
         print()
         print(Fore.RED + "Invalid option")
         print(Style.RESET_ALL)


def basic_calcs(selected_option: int, x: float, y: float) -> None:
   try:
      
      match selected_option:
               case 1:
                  result = add(x, y)
                  print(Fore.GREEN + f"Result: {x} + {y} = {result}")
               case 2:
                  result = sub(x, y)
                  print(Fore.GREEN + f"Result: {x} - {y} = {result}")
               case 3:
                  result = div(x, y)
                  print(Fore.GREEN + f"Result: {x} / {y} = {result}")
               case 4:
                  result= mult(x, y)
                  print(Fore.GREEN + f"Result: {x} * {y} = {result}")
               case 5:
                  result = exp(x, y)
                  print(Fore.GREEN + f"Result: {x} ^ {y} = {result}")
                  
   except ZeroDivisionError as e:
      print(Fore.RED + str(e))
      
   finally:
      print(Style.RESET_ALL)
      
def advanced_calcs(selected_option: int, expression: str) -> None:
   
   match selected_option:
      case 1:
         result = poly_deriv(expression)
         print(Fore.GREEN + f"Result: f(x) = {expression} --> f'(x) = {result}")
      case 2:
         print("Not defined yet")