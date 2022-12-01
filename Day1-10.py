# day 1
print("Hello World")

#

def is_leap(year):
	if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
		print('leap year')
		return True
	else:
		print('not a leap year')
		return False
def days_in_month(year,month):
	 days = [31,28,31,30,31,30,31,31,30,31,30,31]
	 if is_leap(year) and month == 2:
		 return 29
	 return days[month - 1]
year = int(input('enter a year:'))
month = int(input('enter a month:'))
day = days_in_month(year,month)
print(day) 	

#head or tail

import random
sides = random.randint(0,1)
if sides == 1:
  print('head')
else:
   print('tails') 

#random choice

import random
a = ['g','o','k','u','l']
print(random.choice(a))

#password generator

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',' W', 'X', 'Y', 'Z']
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
a = int(input('enter number of letters:'))
b = int(input('enter number of numbers:'))
password = []
for i in range(0,a+1):
  password +=random.choice(letters)
for i in range(0,b+1):
  password +=  random.choice(numbers)
random.shuffle(password)
print(password)  

#bmi calculator

  a=float(input('enter your height in m:'))
  b=float(input('enter your weight in kg:'))
  bmi=round(b/a**2)
  if bmi<18.5:
    print('you are under weight')
  if bmi>18.5 and bmi<25:
    print('you have normal weight')
  if bmi>25 and bmi<30:
    print("you are over weighted")
  if bmi>30 and bmi<35:
    print('you have obese')
  if bmi>35:
    print('you are clinicaly obese')        

#hang man game

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

#caeser ciper encrypt forward

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
dir = input('encrypt or decrypt')
n = int(input('no. of shifts:'))
msg = input('enter a msg:').upper()
def encrypt(a,b):
  empty = ''
  for i in a:
    pos = alphabets.index(i)
    new_pos = pos + b
    new = alphabets[new_pos]
    empty += new
  print(empty) 

#caeser ciper decrypt backward
def decrypt(a,b):
  empty = ''
  for i in a:
    pos = alphabets.index(i)
    new_pos = pos - b
    new = alphabets[new_pos]
    empty += new
  print(empty)   
if dir == 'encrypt':
  encrypt(a=msg,b=n)
else:
  decrypt(a=msg,b=n)


# dictionary
scores = {
    'gokul' : 99,
    'ramesh': 50,
    'siva' : 76,
    'ram'   : 87
}
grades = {}
for i in scores:
  score = scores[i]
  if score > 90:
    grades[i]= 'outstaning'

  elif score > 80:
    grades[i] = 'good'
  else:
    grades[i] = 'need improvement'
print(grades)

# another dict	

scores = {
    'gokul' : {'mine':[2,4,6,7,9,0]},
    'ramesh': 50,
    'siva' : 76,
    'ram'   : 87
}
print(scores.keys())
print(scores.values())
print(scores)
for i in scores: #it just print values
  print(i)

 
	
