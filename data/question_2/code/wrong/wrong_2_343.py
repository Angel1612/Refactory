def unique_day(day, possible_birthdays):
    result = 0
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            result = result + 1
    if result == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    result = 0
    for months in possible_birthdays:
        if months[0] == month:
            result = result + 1
    if result == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    return 
