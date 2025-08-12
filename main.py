from ryanair import Ryanair
from datetime import datetime
from datetime import date

api = Ryanair("GBP")

# Departure airport and date frame
Airport = "MAN"
startDate = date(2025, 8, 12)
endDate = date(2025, 12, 30)
max_price = 150

flights = api.get_cheapest_flights(Airport, startDate, endDate)

for i in range(len(flights)):
    if flights[i].price < max_price and flights[i].destinationFull:
        print(flights[i].destinationFull)
        print(flights[i].price)



