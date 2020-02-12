import math
print('Ethan\'s Paint Job Estimator')

program_run = True

while(program_run):
    while(True):
        try:
            feet = float(input('Enter total amounf of square feet that is needed to be painted '))
            if(feet < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break

    while(True):
        try:
            price = float(input('Enter price of paint '))
            if(price < 0):
                print('Negative values are not allowed')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid')
        else:
            break
        
    
    req_gallons = math.ceil(feet/350)
    hours_of_labor = round(((feet/350) * 6), 1)
    cost_of_paint = round((req_gallons * price),2)
    cost_of_labor = round((hours_of_labor * 62.25),2)
    total_cost = cost_of_labor + cost_of_paint
    
    print('Number of Gallons required: ', req_gallons)
    print('Hours of labor required: ', hours_of_labor)
    print('Total cost of paint: $', cost_of_paint)
    print('Total cost of labor: $', cost_of_labor)
    print('Total cost of paint job: $', total_cost)

    another_one= input('Do you want to do another calculation? (y/n): ')
    if(another_one != 'y'):
            program_run = False
