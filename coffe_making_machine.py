MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,                            
            'milk' : 0,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
   "water": 300, 
   "milk": 200,    
 "coffee": 100,
}

def is_sufficient(order_ingredients):
  is_enough = True
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print("sorry,there is not enough {item}")
      is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_recieved,drink_cost):
  if money_recieved >= drink_cost:
    change = round(money_recieved  - drink_cost, 2)
    print(f'here is the {change} change')
    global profit
    profit += drink_cost
    return True
  else:
    print('sorry there is not enough money.so refunded')  

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")    



is_on =   True

while is_on:
  choice  = input('what u want ? (esperesso/latte/cappuccino):')
  if choice == 'off':
    is_on = False
  elif choice == 'report':
    print(f"milk: {resources['milk']}ml")    
    print(f"water: {resources['water']}ml")
    print(f"coffee: {resources['coffee']}ml")
    print(f'money : $ {profit}')
  else:
    drink = MENU[choice]
    if is_sufficient(drink['ingredients']):
      payment = process_coins()
      if is_transaction_successful(payment , drink['cost']):
        make_coffee(choice ,drink["ingredients"])
    

