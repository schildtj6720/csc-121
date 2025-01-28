# A project that utilizes loop and decision structures while adding onto page 44 of the textbook.
# 1/25/2025
# CSC121 m1Lab1– Review
# Jasmine Schildt

# a function is made to recieve the amount of items a user has and to calculate the overall costs
# the results are displayed and the user is asked if they would like to run the program again
# the program ends with a "Thank you!" if the loop_question input value is set to 'No'


def cost_calculation():
    item_amount = int(input('Enter # of items: '))
    
    print()
    
    if item_amount >= 1 and item_amount <= 19:
        cost_per_item = 4.75
        item_cost = item_amount * cost_per_item
    elif item_amount >= 20 and item_amount <= 49:
       cost_per_item = 4.50
       item_cost = item_amount * cost_per_item
    elif item_amount >= 50 and item_amount <= 99:
        cost_per_item = 4.25
        item_cost = item_amount * cost_per_item
    elif item_amount >= 100:
        cost_per_item = 4.00
        item_cost = item_amount * cost_per_item
            
    print(f'Cost per item = ${cost_per_item:.2f}')
    print(f'Total order cost = ${item_cost:.2f}')
    
    print()
    
    loop_question = input('Would you like to run again? Enter Yes or No: ')
    print()
    
    return loop_question

loop_question = input('Would you like to run again? Enter Yes or No: ')

while loop_question == 'Yes':
    cost_calculation()
    loop_question = cost_calculation()
else:
    print('Thank you!')
