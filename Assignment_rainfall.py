#PART 1 - select all measurements using Seattle code; sum all measurements for each month for that location; save results as json file

#first make a dictionary with all the seattle entries
import json

with open('stations.csv') as file:
    stations = {}
    next(file)
    for line in file:
        (Location, State, Station) = line.strip().split(',')
        stations[Location] = {
            'State' : str(State),
            'Station' : str(Station)
        }
seattle_code = stations['Seattle']['Station']
print('The code for Seattle is: ' + str(seattle_code) + ' .')           #code up to here extracts the code for Seattle; it also creates a dictionary of stations.csv with the city names as keys

#print(stations)
seattle_month = [0]*12                                                   #list has 12 entries, one for each month (0 is jan, 1 is feb etc)
with open('precipitation.json') as file:
    precipitation = json.load(file)
    for item in precipitation:                                           #loops through every entry in the list of dictionaries
        if item['station']==seattle_code:                                #if the station is in seattle, take the value of precipitation and add it to the appropriate part in the list seattle_month
            month = int(item['date'].split('-')[1])
            seattle_month[month-1] += item['value']
           

print(seattle_month)

with open('monthly_precipitation.json', 'w') as file:
    json.dump(seattle_month, file, indent=4)

###PART 2 - find total precipitation, then find composition of participation per month

total_precipitation = int(sum(seattle_month))
print('The total precipitation is: ' + str(total_precipitation) + ' in a unit that is not specified!')

#to find the composition, just devide every entry in list seattle_month by total population and then multiply all by 100 - should werq amirite?

proportion = [100*x/total_precipitation for x in seattle_month]          #loops through seattle_month and multiplies each value by 100/total_precipitation - stores new values in a list called proportion, which gives how much of the yearly rain happens that specific month
print(proportion)

























#for item in precipitation:
#    if item['station']==seattle_code:
#        seattle_month[int(date.split('-')[5:7])-1] += value
#        #if item[int(date.split('-')[5:7])]

#print(seattle_month)

'''
seattle = [203, 183, 41, 2, 41]

When looking at a measuremet, check that it is for Seattle, find the month, find the rainfall, add rainfall to correct element in seattle list.


'''