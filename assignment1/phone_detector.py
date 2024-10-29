import re

def detect_phone(text):
    '''This function detects phone numbers entities from a text'''
    phone_number_pattern = re.compile(r'(\+\d{1,2}\s?)?(\()?(\d{3})(?(2)\))[-.\s]?(\d{3})[-.\s]?(\d{4})')
    matches = phone_number_pattern.finditer(text)
    phone_numbers = [match.group(0) for match in matches]
    return phone_numbers

def censor_phone(text, stats):
    '''This function detects phone numbers from a text and censors them with special characters'''
    phone_numbers = detect_phone(text)
    for number in phone_numbers:
        text = text.replace(number, 'X' * len(number))
    stats['phones masked'] = len(phone_numbers)
    return text, stats


