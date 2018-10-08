# from pandas.tseries.offsets import BMonthEnd
# from datetime import date,timedelta

# d=date.today()-timedelta(days=15)
# dateThatDay=d.day
# print(dateThatDay)
# # print(d)
# # d='2018-09-08'
# offset = BMonthEnd()
# print(offset.rollforward(d))
#Last day of current month
# offset.rollforward(d)
from pandas import BMonthEnd
from datetime import date

d=date.today()

offset = BMonthEnd()

#Last day of current month
print(offset.rollforward(d))

#Last day of previous month
offset.rollback(d)
