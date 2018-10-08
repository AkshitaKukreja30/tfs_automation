# thursday=3
# friday=4
# sat=5
# sun=6
# mon=0
# tues=1
# wednesday=2
import datetime

print(datetime.datetime.today().weekday())
dayBeingChecked = datetime.datetime.today().weekday()

if(dayBeingChecked==5) or (dayBeingChecked==6):
	print("weekend")

else:
	print("weekday")
	if(dayBeingChecked==0):
		iterationFrom=datetime.date.today().day
		iterationFromFullDate=datetime
		
	elif(dayBeingChecked==1):
		iterationFrom=datetime.date.today().day-1
		
	elif(dayBeingChecked==2):
		iterationFrom=datetime.date.today().day-2
		
	elif(dayBeingChecked==3):
		iterationFrom=datetime.date.today().day-3
		
	elif(dayBeingChecked==4):
		iterationFrom=datetime.date.today().day-4










i=0;
if(datetime.date.today().month==1):
		month[i]='JANUARY'
		i=i+1
elif(datetime.date.today().month==2):
		month[i]='FEBRUARY'
		i=i+1
elif(datetime.date.today().month==3):
		month[i]='MARCH'
		i=i+1
elif(datetime.date.today().month==4):
		month[i]='APRIL'
		i=i+1
elif(datetime.date.today().month==5):
		month[i]='MAY'
		i=i+1
elif(datetime.date.today().month==6):
		month[i]='JUNE'
		i=i+1
elif(datetime.date.today().month==7):
		month[i]='JULY'
		i=i+1
elif(datetime.date.today().month==8):
		month[i]='AUGUST'
		i=i+1
elif(datetime.date.today().month==9):
		month[i]='SEPTEMBER'
		i=i+1
elif(datetime.date.today().month==10):
		month[i]='OCTOBER'
		i=i+1
elif(datetime.date.today().month==11):
		month[i]='NOVEMBER'
		i=i+1
elif(datetime.date.today().month==12):
		month[i]='DECEMBER'
		i=i+1

iterationTo = iterationFrom + 4
if(iterationFrom>=28):
	datetime.date.today().month==1
print(month,"",iterationFrom,"TO",month,"",iterationTo)


# print(datetime.date.today())
# print(datetime.date.today().month)
# print(datetime.date.today().day)