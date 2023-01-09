import datetime
currdy=datetime.date.today()
print(currdy)
format=datetime.date.strftime(currdy,"%-%m-%y")
print(format)