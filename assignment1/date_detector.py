import datefinder

def replace_with_x(input_string, start_index, end_index):
    return input_string[:start_index] + 'X' * (end_index - start_index) + input_string[end_index:]


def censor_date(text, stats):
    '''This function detects dates from a text and censors them with special characters'''
    matches = datefinder.find_dates(text, index=True)
    c = 0
    for match, indices in matches:
        c+=1
        match_start = indices[0]
        match_end = indices[1]
        text = replace_with_x(text, match_start, match_end)
    stats['dates masked'] = c
    return text, stats



