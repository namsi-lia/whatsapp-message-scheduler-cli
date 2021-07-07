
import date_time
import phonenumber_check
import whatsapp_schedule_message
from pyfiglet import Figlet
from termcolor import colored

#display screen name
f = Figlet(font='slant')
print('----------------------------------------------------------------------------------------')
print(colored(f.renderText('WHATSAPP MESSAGE SCHEDULER'),'blue'))
print('Author:Namsi Lydia')
print('\n''-------------------USAGE--------------------')
print('1."To run app:cd /App/inputs/python3 main.p"')
print('2."To test application test:command:coverage run -m unittest whatsapp_schedule_test.py "')
print('----------------------------------------------------------------------------------------')


# user prompted to input recipient's number
def enter_number():
    recipient_number = input("Enter recipient's number(International format e.g +254**********): +")

    # validate recipient's number
    is_valid_number = phonenumber_check.check_phone_number(recipient_number)

    # Loop to request for correct number format in case of validation
    while not is_valid_number:
        recipient_number = input("Invalid Number! Please try again. Enter recipient's number: +")
        is_valid_number = phonenumber_check.check_phone_number(recipient_number)

    return recipient_number


def input_date_option():
    when_date = input("Choose the  DATE do you want to send the message:\n 1. Today \n 2. Set a date\n")
    is_valid_choice = phonenumber_check.check_options(when_date)
    while not is_valid_choice:
        when_date = input("Invalid Choice! Please select \"1\" or \"2\" \nWhat DATE do you want to send the "
                          "message:\n 1. Today \n 2. Set a date\n")
        is_valid_choice =phonenumber_check.check_options(when_date)
    return when_date


def enter_send_time():
    send_time = input("Please Enter the time to send message (Use 24-format e.g HH:MM): ")
    valid_time_format = date_time.check_time_format(send_time)
    while not valid_time_format:
        send_time = input("Invalid Time! Please Enter the time to send message (Use 24-format e.g HH:MM): ")
        valid_time_format = date_time.check_time_format(send_time)
    return send_time


def enter_date():
    send_date = input("Please Enter the date to send message (In the format e.g dd/mm/yyyy): ")
    valid_date_format = date_time.check_date_format(send_date)
    while not valid_date_format:
        send_date = input(
            "Invalid Date! Please Enter the date to send message (In the format e.g dd/mm/yyyy): ")
        valid_date_format = date_time.check_date_format(send_date)
    return send_date

def main():
    # message to send
    message = input("Enter message to send: ")

    # recipient's number
    recipient_number = enter_number()

    # ask user whether to select option of when to send date
    when_date = input_date_option()

    if when_date == "1":
        # ask user to enter time
        send_time = enter_send_time()
        date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
        send_date_time = date_time.get_todays_date() + " " + send_time
        valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)
        while not valid_time:
            print("ERROR! The time entered has already passed!")
            send_time = enter_send_time()
            date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
            send_date_time = date_time.get_todays_date() + " " + send_time
            valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)


    elif when_date == "2":
        # user inputs date
        send_date = enter_date()
        valid_date = date_time.check_date_not_passed(date_time.get_todays_date(), send_date)
        while not valid_date:
            print("ERROR! The date entered has already passed!")
            send_date = enter_date()
            valid_date = date_time.check_date_not_passed(date_time.get_todays_date(), send_date)
        if valid_date:
            send_time = enter_send_time()
            date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
            send_date_time = send_date + " " + send_time
            valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)
            while not valid_time:
                print("ERROR! The time  entered has already passed!")
                send_time = enter_send_time()
                date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
                send_date_time = send_date + " " + send_time
                valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)

    date_time.countdown_timer(date_time_now, send_date_time)
    if whatsapp_schedule_message.schedule_message(message, recipient_number):
        data = [date_time_now, message, recipient_number, send_date_time]
       


if __name__ == "__main__":
    main()
    
