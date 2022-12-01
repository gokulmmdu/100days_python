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


 
	
