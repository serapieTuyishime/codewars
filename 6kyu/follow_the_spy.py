# We are diligently pursuing our elusive operative, Matthew Knight, who also goes by the alias Roy Miller.
# He employs a nomadic lifestyle to evade detection, constantly moving from one location to another,
# with each of his journeys following a perplexing and non-standard sequence of itineraries.
# Our mission is to decipher the routes he will undertake during each of his voyages.
#
# Task
# You've been provided with an array of itinerary routes, decipher the precise destinations he will visit
# in the correct sequence according to his meticulously planned itineraries.
#
# Example
# Based on the provided routes:
#
# [ [USA, BRA], [JPN, PHL], [BRA, UAE], [UAE, JPN] ]
# The correct sequence of destinations is:
#
# "USA, BRA, UAE, JPN, PHL"
# Note:
#
# You can safely assume that there will be no duplicate locations with distinct routes.
# All routes provided will have non-empty itineraries.
# There will always be at least one (1) route connecting one waypoint to another.
# Steps to solving it


# We have start and destination.
# Once you have destination, it becomes the start of another trip.
# Follow this until the destination becomes the start of another trip

from itertools import chain
from collections import Counter

def find_routes(routes):
    result_routes = []
    # Count all the unique cities
    all_routes_count = len(set(chain(*routes)))
    count = 0

    # Find the start (the one that does not appear as a destination anywhere)
    cities_count = dict(Counter(chain(*routes)))
    one_apperarances = [city[0] for city in cities_count.items() if city[1] == 1]
    try:
        next(i for i,x in enumerate(routes) if x[0] == one_apperarances[0])
    except StopIteration:
        start_one = one_apperarances[1]
        print("No routes found")
        pass
    else:
        start_one = one_apperarances[0]

    # Do the actual ordering
    result_routes.append(start_one)
    while len(result_routes) != all_routes_count:
        start = result_routes[-1]
        try:
            start_index  = [i for i, x in enumerate(routes) if x[0] == start][0]
        except StopIteration:
            start_index = [i for i, x in enumerate(routes) if x[0] == start][1]
            print("No routes found",start_index, start)
        else:
            destination = routes[start_index][1]
            # if destination not in result_routes:
            result_routes.append(destination)
            start = destination

        count += 1
        if count == 30:
            break
    return result_routes

# print(find_routes([('two','three'), ('one','two')]))  # One two three
print(find_routes([('Chicago','Winnipeg'), ('Halifax','Montreal'), ('Montreal','Toronto'), ('Toronto','Chicago'), ('Winnipeg','Seattle')]))
#  'Halifax, Montreal, Toronto, Chicago, Winnipeg, Seattle'
# print(find_routes([ ["USA", "BRA"], ["JPN", "PHL"], ["BRA", "UAE"], ["UAE", "JPN"] ]))  # One two three