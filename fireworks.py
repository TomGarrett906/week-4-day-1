'''A city is putting on a fireworks show for the 4th of July. There are `n` types of fireworks, and for each type, theres a specific amount of time it takes to launch that firework.

The city wants to put on a show that lasts for `m` minutes.The function `create_show` takes a list of fireworks (each represented as an integer indicating the time in minutes it takes to launch) and a total time for the show `m`.

 The function will return a list of fireworks that will fill the shows time as evenly as possible.

Heres the Python function:
'''
import random 
#O(log(N))??? For the function becuase we are dealing with a list that we can keep returning to until we escape it.
#It feels linear at first with the coorealtion between the input of firework time and show time remaining.  Not 100% sure because it can be sort of like that binary thing if we are not given a time constraint for our fireworks show??
def create_show(fireworks, show_time): # O(N) Because we're dealing with a list

    fireworks.sort()# O(N) Puts the firework time in order,iterating from least to greatest time

    show = [] #O(1) #Create an empty list (constant) to store to fireworks into later

    remaining_time = show_time #O(1) Time left is our showtime

    while remaining_time > 0 and fireworks: #O(N) While the show is still going, so iterating continously 
           # Select a random firework

        firework = random.choice(fireworks) #O(N)? Not sure.. Maybe it has to go through a list from randome module?

        if firework <= remaining_time: #O(1) Constant just once OR, O(N)if is theres enough time for another firework again?
               # Add the firework to the show

            show.append(firework) # O(1)  Append it to our show list

            remaining_time -= firework # O(1) Constant

        else:
              # This firework is too long, remove it from consideration

            fireworks.remove(firework) #O(1) Can happen more than once

    return show #O(1) Just checks, a constant

