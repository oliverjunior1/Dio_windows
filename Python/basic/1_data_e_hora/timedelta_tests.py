from datetime import datetime, timedelta

x = datetime.now()
print(x)

y = x+timedelta(weeks=1)

print(y)