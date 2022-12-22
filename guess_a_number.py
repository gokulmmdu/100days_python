#guessing number 

import random
def func():
  n = random.randint(1,10)
  print(n)
  flag = 'False'
  while flag == 'False':
    print(' welcome to guessing number game ')
    choice = str(input('do u want easy or hard:')).lower()
    if choice == 'easy':
      chance = 5
      for i in range(chance):
        print(f"you have {chance} chances ")
        chance -= 1
        if chance < 0:
          print('you lose')
          flag = 'True'   
        a = int(input('enter a number:'))
        if n == a:
          print('you win') 
          flag = 'True'
        elif n > a:
          print('low')
        elif n < a:
          print('high')
    elif choice == 'hard':
      chance = 3
      for i in range(chance):
        print(f"you have {chance} chances ")
        chance -= 1
        if chance < 0:
          print('you lose')
          flag = 'True'   
        a = int(input('enter a number:'))
        if n == a:
          print('you win') 
          flag = 'True'
        elif n > a:
          print('low')
        elif n < a:
          print('high')     
func()
  

