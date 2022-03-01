# Traveling list

from operator import truediv
from pickle import TRUE


places = (input("Name your dream place to travel: "))
live = (input("Would you live here? "))
num_place = []

travel_list = {
    "Italy": "I could live here",
    "Spain": "I would love to experience their foods",
    "Japan": "A must see",
    "Scotland": "Maybe I would live here"
}


def travel_places(num_place, places):
    if num_place == travel_list.index("Italy"):
        places = num_places + travel_list
        destination = input("Would you live here?")


to_continue = TRUE

while to_continue:
    places = travel_list
    num_places = (input("What is you dream number of travel? "))
    if num_place < 10:
        travel_list[places] = "Awesome, sounds like you love to travel!"
    elif num_place < 1:
        travel_list[places] = "Fantastic!"
    else:
        travel_list[places] = False
        print(f"We need to get you traveling.  {places}")
print(F"You will have lots of fun {places}")