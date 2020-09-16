import requests
from pprintpp import pprint
from datetime import date

today = date.today()
# print(today.day)
a = today
print("Current date is = ", a)
print("Extracted Day From Current Date Is = ", today.day)

# create variable and store day
day = a.day

# If given number is greater than 1
if day > 1:
    for i in range(2, day):
        if (day % i) == 0:
            print(day, "is not a prime number")
            print("Date is not prime so no date")
            break

        else:
            print(day, "is a prime number")
            url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=f46c4757ae895b898f53d9046f29c795'
            res = requests.get(url)
            data = res.json()
            pprint(data)
            break
