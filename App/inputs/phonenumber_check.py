import numbers
# function to validate number supplied by user
def check_phone_number(phonenumber):
    is_valid = False
    try:
        phonenumber = int(phonenumber)
    except ValueError as e:
        is_valid = False
    else:
        if isinstance(phonenumber, numbers.Number):
            if 8 < len(str(phonenumber)) < 16:
                is_valid = True
    return is_valid


# Check options of when to send message
def check_options(choice):
    valid_choice = False
    if choice == "1" or choice == "2":
        valid_choice = True
    return valid_choice