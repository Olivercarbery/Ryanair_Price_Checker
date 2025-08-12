from ryanair import Ryanair
from datetime import timedelta
from datetime import date

api = Ryanair("GBP")

# Departure airport and departure date frame
Airport1 = "MAN"
Airport2 = "LPL"

startDate = date(2025, 8, 12)
endDate = date(2025, 12, 30)
max_price = 150
trip_length = 7

flights = api.get_cheapest_flights(Airport1, startDate, endDate)

# loop through all the flights found and filter for price and not in the UK
for i in range(len(flights)):
    if flights[i].price < max_price and "United Kingdom" not in flights[i].destinationFull:
        # Print flight data to console
        print(f'{Airport1} to {flights[i].destinationFull}')
        print(f'Outbound Flight Price: £{flights[i].price}')
        print(f'Outbound Flight Date: {flights[i].departureTime}')

        # Use trip length to find cheap return flights
        returnFlight = api.get_cheapest_flights(flights[i].destination, flights[i].departureTime+timedelta(days=trip_length), flights[i].departureTime + timedelta(days=trip_length))
        for j in range(len(returnFlight)):
            if returnFlight[j].destination == Airport1:
                # Print return flight data
                print(f'Return to {Airport1} Flight Price: £{returnFlight[j].price}')
                print(f'Return to {Airport1} Flight Time: {returnFlight[j].departureTime}')
                print(f'{Airport1} Total Price: £{flights[i].price+returnFlight[j].price}')

            if returnFlight[j].destination == Airport2:
                print(f'Return to {Airport2} Flight Price: £{returnFlight[j].price}')
                print(f'Return to {Airport2} Flight Date: {returnFlight[j].departureTime}')
                print(f'{Airport2} Total Price: £{flights[i].price+returnFlight[j].price}')

    print('\n'*2)
print('\n'*5)
print(f'~~~~~~~ Flights from {Airport2} ~~~~~~~')
flights = api.get_cheapest_flights(Airport2, startDate, endDate)
for i in range(len(flights)):
    if flights[i].price < max_price and "United Kingdom" not in flights[i].destinationFull:
        print(f'{Airport2} to {flights[i].destinationFull}')
        print(f'Outbound Flight Price: £{flights[i].price}')
        print(f'Outbound Flight Time: {flights[i].departureTime}')

        returnFlight = api.get_cheapest_flights(flights[i].destination, flights[i].departureTime + timedelta(days= trip_length), flights[i].departureTime + timedelta(days=trip_length))

        for j in range(len(returnFlight)):
            if returnFlight[j].destination == Airport2:
                print(f'Return to {Airport2} Flight Price: £{returnFlight[j].price}')
                print(f'Return to {Airport2} Flight Time: {returnFlight[j].departureTime}')
                print(f'{Airport2} Total Price: £{flights[i].price+returnFlight[j].price}')

            if returnFlight[j].destination == Airport1:
                print(f'Return to {Airport1} Flight Price: £{returnFlight[j].price}')
                print(f'Return to {Airport1} Flight Time: {returnFlight[j].departureTime}')
                print(f'{Airport1} Total Price: £{flights[i].price+returnFlight[j].price}')
    print('\n')
