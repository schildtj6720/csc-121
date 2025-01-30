# The vehicle routing excersice from page 63 of the textbook. An assignment that practices use of loops and decision structures.
# 1/29/25
# CSC121 m1Lab2– Review
# Jasmine Schildt

# route_num and more_routes values are established to start the program smoothly
# empty lists are created
# while function is created (route_num is appended to route_num_list, user is asked for distance and speed, time is calculated, user is asked if they want to add more routes).
# fastest route time and index are found
# results are displayed

route_num = 0
more_routes = 'y'

time_list = [ ]
route_num_list = [ ]

while more_routes == 'y':
    route_num = route_num + 1
    route_num_list.append(route_num) 
    
    distance = float(input(f'Enter route {route_num} distance: '))
    while distance == 0 or distance < 0:
        distance = float(input(f'Invalid value! Enter again: '))
   
    speed = float(input(f'Enter route speed {route_num} distance: '))
    while speed == 0 or speed < 0:
        speed = float(input(f'Invalid value! Enter again: '))
    
    time_calculated = (distance / speed) * 60
    time_list.append(time_calculated)
    
    more_routes = input('More routes? (y/n)?: ')
    print( )
 
fastest_route_time = min(time_list)
fastest_route_index = int(time_list.index(fastest_route_time))

fastest_route_num = route_num_list[fastest_route_index]
fastest_route_time = int(fastest_route_time)


print(f'Route {fastest_route_num} is fastest; {fastest_route_time} minutes')
