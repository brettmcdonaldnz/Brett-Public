# BRETT MCDONALD
# SID 10158931
# Assignment 1B
# Question 3: Generate real estate advertisements (6 marks)

import random

description = ['First', 'Dream', 'New Family', 'Brand New']
adjective = ['Wonderful', 'Sunny', 'Spacious', 'Secluded']
bedrooms = [1, 2, 3, 4, 5]
suburb = ['Hokowhitu', 'Fitzherbert', 'Cloverlea', 'Terrace End', 'Kelvin Grove']
type_of_owner = ['a couple', 'a family', 'a retired couple', 'a large family', 'a professional couple']
amenities_close_by = ['great schools', 'shopping centre', 'motorway', 'airport', 'hospital']

def real_estate_ad():
    print ("*** Your {0} Home ***".format(random.choice(description)))
    print ("{0} {1} bedroom home in {2}".format(random.choice(adjective), random.choice(bedrooms),random.choice(suburb)))
    print ("Would suit {0}".format(random.choice(type_of_owner)))
    print ("Close to {0}.".format(random.choice(amenities_close_by)))
    print ("All enquires to Joe Bloggs on 007 1234")
    print ("*** Make it yours today! ***")

real_estate_ad()

# # RESULT
# *** Your Brand New Home ***
# Sunny 3 bedroom home in Kelvin Grove
# Would suit a large family
# Close to motorway.
# All enquires to Joe Bloggs on 007 1234
# *** Make it yours today! ***
