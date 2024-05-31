def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    miles = 100000 / 1609.344
    
    return miles/gallon


def miles_gallon_to_liters_100km(miles):
    km = miles * 1609344
    liters = 1 *3.785411784
    
    return liters/km

