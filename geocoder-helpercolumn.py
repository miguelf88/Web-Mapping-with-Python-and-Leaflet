import geopy
import pandas as pd
from geopy.geocoders import Nominatim


def main():
    io = pd.read_csv('census_country.csv', index_col=None, header=0, sep=',')

    def get_latitude(x):
        return x.latitude

    def get_longitude(x):
        return x.longitude

    geolocator = Nominatim(user_agent='my-geocoder')

    io['helper'] = io['Area_Name'].map(str) + " " + io['Country'].map(str)
    geolocate_column = io['helper'].apply(geolocator.geocode)
    io['latitude'] = geolocate_column.apply(get_latitude)
    io['longitude'] = geolocate_column.apply(get_longitude)
    io.to_csv('geocoding-output-helper.csv')


if __name__ == '__main__':
    main()
