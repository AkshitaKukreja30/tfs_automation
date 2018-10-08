from datetime import date,timedelta
dateBeingCheckedFor = date.today()+timedelta(days=42)
dayOfWeek = dateBeingCheckedFor.weekday()
if(dayOfWeek>=5):
	print("weekend")
else:
	iterationFromFullDate=dateBeingCheckedFor-timedelta(days=dayOfWeek)
	iterationToFullDate=iterationFromFullDate+timedelta(days=4)
	if 4 <= iterationFromFullDate.day <= 20 or 24 <= iterationFromFullDate.day <= 30:
	    suffix1 = "th"
	elif iterationFromFullDate.day % 10 is 2:
		suffix1 = "nd"
	elif iterationFromFullDate.day % 10 is 3:
		suffix1 = "rd"
	elif iterationFromFullDate.day % 10 is 1:
		suffix1 = "st"

	if 4 <= iterationToFullDate.day <= 20 or 24 <= iterationToFullDate.day <= 30:
		print ("life is still good")
	elif iterationToFullDate.day % 10 is 2:
	    suffix2 = "nd"
	elif iterationToFullDate.day % 10 is 3:
		suffix2 = "rd"
	elif iterationToFullDate.day % 10 is 1:
		suffix2 = "st"
	print(iterationFromFullDate.strftime("%B"),iterationFromFullDate.day,suffix1,"To",iterationToFullDate.strftime("%B"),iterationToFullDate.day,suffix2)

