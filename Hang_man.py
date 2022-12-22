import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end = False
life = 6  
list1 = ['gokula','siva','ramesh']
sys=random.choice(list1)
op = []
for i in range(len(sys)):
  op += '+'
while not end:
  user=input('guess the letter:').lower()
  for i in range(len(sys)):
    l=sys[i]
    if l == user:
      op[i] = l 
      print(op) 
  if user not in sys:
    life -= 1
    if life == 0:
      print('you lose')
      end = True 
  print(op)   
  if '+' not in op:
    end = True
    print('you win')
  print(stages[life])



