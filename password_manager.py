import time
from colorama import Fore
valid_options = ["Add ","Veiw","Quit"]
intro = print(Fore.CYAN +""" 
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █▀▄ By Ritvik Bisht.
""")
time.sleep(2)
print("""\n\n This a program based to store your passwords as you might forget them in future!\n\n\n""")

def view():
    with open ('storage.txt','r') as f:
        print('Opening the file...')
        time.sleep(1)
        for line in f.readlines():
            print(line)
            time.sleep(1)
            print('Read the data!')

def add():
    user_name = input('Account Name : ')
    user_pass = input('Password : ')
    #user_mail = input('Do you wish to add any e-mail? [Yes/No]')
    #if user_mail == "no":
     #   user_mail = "No mail provided"
    #elif user_mail == "yes":
     #   user_mail = input('E-mail : ')
    with open ('storage.txt', 'a') as f:
            f.write(f'Name : {user_name}| Password : {user_pass}\n')
            print('Storing...')
            time.sleep(1)
            print('The data has been stored\n\n\n')








while True:
    mode = input("Would you like to store a fresh password or veiw a stored password? [add/veiw] | Type quit to quit the program  ")
    if mode == "quit":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "quit":
        break
    else:
        print(f'Invalid Command : Available commands = {valid_options}') 
        continue
