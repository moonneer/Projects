from CSE8ACSV import *

blm_protest_data = get_blm_data("blm_state.csv")
state_populations = get_state_pops()

def separate_data(blm_protest_data):
    output = ([], [])
    for dictionary in blm_protest_data:
        if dictionary['TotalProtests'] > 0:
            output[0].append(dictionary['State'])
        elif dictionary['TotalProtests'] == 0:
            output[1].append(dictionary['State'])
    return output

def average_rates(states_list, field, blm_protest_data):
    total = 0
    for dictionary in blm_protest_data:
        if dictionary['State'] in states_list:
            total += dictionary[field]
    return total/len(states_list)

def compare_rates(field, blm_protest_data):

    protest_list = separate_data(blm_protest_data)
    states_with_protest = average_rates(protest_list[0], field, blm_protest_data)
    states_without_protest = average_rates(protest_list[1], field, blm_protest_data)

    if states_with_protest > states_without_protest:
        return 'States with BLM protests have a higher ' + field
    elif states_without_protest > states_with_protest:
        return 'States without BLM protests have a higher ' + field
