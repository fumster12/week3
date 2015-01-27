# Divvy Bikes by Funmi Dosunmu 1/27/15
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']
young_lat = 41.793414
young_lon = -87.600915

for station in stations:
    StationId = station['id']
    Latitude = station['latitude']
    Longitude = station['longitude']
    Name = station['stationName']
    Bikes = station['availableBikes']
    x = (Latitude)
    y = (Longitude)5
    d = math.sqrt(((young_lat - x)(young_lat - x)) + ((young_lon - y)(young_lon-y)))
    
    
print('The station closest to Young is', Name,'and there are', Bikes, 'bikes available.')


##def distance():
##    d = 0
##    for station in stations:
##    young_lat = 41.793414
##    young_lon = -87.600915
##    x = min(Latitude)
##    y = min(Longitude)
##    d = sqrt(((young_lat - x)(young_lat - x)) + ((young_lon - y)(young_lon-y)))
##    x = min(Latitude)
##    y = min(Longitude)
##    return d


    






# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes
## like x and y coordinates, and calculate distance between locations with
## the usual Euclidean distance formula.

# 1. Modify the code above to display the station name and number of available
## bikes for the station closest to Young.

# You will likely want to consult the JSON stream from Divvy

# - http://www.divvybikes.com/stations/json
