# this is a dumb idea and probs a waste of time but
# while im in the genshin hole
# and the website i usually use to track my pity is down
# i am going to try to code something
# wish (haha get it) me luck
# im going to steal a lot from my old cs 8 final mwahaha

# standard banner pity recorder / calculator??
# 5 star: guaranteed in 90 pulls
# 4 star: guaranteed in 10 pulls

def print_menu(user_menu):
    print("Main menu:")
    for key, value in user_menu.items(): 
        print('{} - {}'.format(key,value)) 

def check_option(option,menu):
    if (type(option) == int) or (option.isdigit() == True):
        if option in menu:
            return 'valid'
        else:
            print('Hey! {} is an invalid option.'.format(option))
            print('Please enter a valid option.') 
            return 'invalid'
    else:
        print('Hey! {} is not an integer.'.format(option))
        print('Please enter an integer.') 
        return 'invalid'
    
# option 1
def valid_stars(wish):
    if (wish == "3") or (wish == "4") or (wish == "5"):
        return True
    else:
        return False

def star_checker(wish):
    while True:
        if valid_stars(wish) == False:
            print(f"There's no such thing as a {wish} star wish.")
            print("Would you like to change this entry? (Y/N)")
            user_choice = input("> ")
            if user_choice == "Y":
                print("Enter the new value for this entry:")
                new_entry = input("> ")
                wish = new_entry
                continue
            else:
                return None
        elif valid_stars(wish) == True:
            return True

def data_entry():
    print("Enter how many stars each of your wishes has, separated by a space:")
    user_input = input("> ")
    user_list = user_input.split()
    for (index,entry) in enumerate(user_list):
        if star_checker(entry) == True:
            user_list[index] = entry
    return user_list

# option 2
def add_data(user_list):
    print("Would you like to add wishes? (Y/N)")
    user_choice = input("> ")
    if user_choice == "Y":
        print("Enter the rarities of the wishes you would like to add, separated by a space:")
        user_input = input("> ")
        input_list = user_input.split()
        for entry in input_list:
            user_list.append(entry)
        return user_list
    else:
        return None

# option 4
def update_data(user_list):
    print("Would you like to update wishes? (Y/N)")
    user_choice = input("> ")
    if user_choice == "Y":
        print("These are the current wishes:")
        print(user_list)
        print("How many wishes would you like to update? (number pls)")
        user_input = int(input("> "))
        for i in range(user_input):
            print("Enter the index number you would like to update: (ex. first wish is 1)")
            user_index = int(input("> "))
            print("Enter the new value for this position:")
            user_entry = input("> ")
            user_list[user_index-1] = user_entry
    else:
        return None

# option 5
def delete_data(user_list):
    print("Would you like to delete wishes? (Y/N)")
    user_choice = input("> ")
    if user_choice == "Y":
        print("These are the current wishes:")
        print(user_list)
        print("How many wishes would you like to delete? (number pls)")
        user_input = int(input("> "))
        for i in range(user_input):
            print("Enter the index number you would like to delete:")
            user_index = int(input("> "))
            del user_list[user_index-1]
            print('Deleted!')
    else:
        return None

# option 6
def total_wishes(user_list):
    wishcount = len(user_list)
    return wishcount

def four_star_pity(user_list):
    #if there is a 4 in the list,
        #have one pointer at the first 4 in the list,
        #and count the number of entries until you reach another 4. (reset)
        #return number of entries after the 4.
    #else if there is no 4 in the list,
        #count from beginning of list.
    user_pity = 0
    for (index,entry) in enumerate(user_list):
        if entry == '4':
            user_pity = 0
            continue
        else:
            user_pity += 1
            continue
    return user_pity

def five_star_pity(user_list):
    #if there is a 5 in the list,
        #have one pointer at the first 5 in the list,
        #and count the number of entries until you reach another 5. (reset)
        #return number of entries after the 5.
    #else if there is no 5 in the list,
        #count from beginning of list.
    user_pity = 0
    for (index,entry) in enumerate(user_list):
        if entry == '5':
            user_pity = 0
            continue
        else:
            user_pity += 1
            continue
    return user_pity

def four_star_counter(user_list):
    four_stars = 0
    for (index,entry) in enumerate(user_list):
        if entry == "4":
            four_stars += 1
    return four_stars

def five_star_counter(user_list):
    five_stars = 0
    for entry in user_list:
        if entry == "5":
            five_stars += 1
    return five_stars

def wish_stats(user_list):
    wish_total = total_wishes(user_list)
    four_star_total = four_star_counter(user_list)
    five_star_total = five_star_counter(user_list)
    user_4starpity = four_star_pity(user_list)
    user_5starpity = five_star_pity(user_list)
    print("You have made a grand total of",wish_total,"wishes.")
    print(f"({wish_total * 160} primogems)")
    print("You have pulled a total of",four_star_total,"four stars, and a total of",five_star_total,"five stars.")
    print("You are at",user_4starpity,"four star pity, so you need",(10-user_4starpity),"more wishes to get your next guaranteed four-star.")
    if user_4starpity >= 8:
        print("You are also around four-star soft pity, so you should get one very soon.")
    print("You are at",user_5starpity,"five star pity, so you need",(90-user_5starpity),"more wishes to get your next guaranteed five-star.")
    if user_5starpity >= 75:
        print("You are also around five-star soft pity, so you should get one very soon.")
        
#option 7
def load_data(user_list):
    import csv
    import os
    filename = 'wish_data.csv'
    print(f"Load the default file ({filename})? (Y/N)")
    user_choice = input('> ')
    if user_choice == 'Y':
        while True:
            if not os.path.isfile(filename):
                print(f"WARNING: Cannot find a CSV file named '{filename}'")
                print('::: Enter the name of an existing csv file.') #if default file doesnt exist
                user_file = input('> ')
                continue
            print(f"Reading the database from {filename}")
            new_list = load_list_from_csv(filename)
            print("Resulting database:\n", new_list)
            for entry in new_list:
                user_list.append(entry)
            break
    elif user_choice == 'N':
        print('::: Enter the name of the csv file to load.')
        user_file = input('> ')
        while True:
            if '.csv' != user_file[-4:]:
                print(f'WARNING: {user_file} does not end with `.csv`')
                print('::: Enter the name of an existing csv file.')
                user_file = input('> ')
                continue
            elif not os.path.isfile(user_file):
                print(f"WARNING: Cannot find a CSV file named '{user_file}'")
                print('::: Enter the name of an existing csv file.')
                user_file = input('> ')
                continue
            else:
                print(f"Reading the database from {user_file}")
                new_list = load_list_from_csv(user_file)
                print("Resulting database:\n", new_list)
                for entry in new_list:
                    user_list.append(entry)
            break

def load_list_from_csv(filename):
    new_list = []
    with open(filename, 'r') as file:
        read_file = csv.reader(file)
        if read_file == []:
            return []
        else:
            for row in read_file:
                for cell in row:
                    new_list.append(cell)
    return new_list

# option 8
import csv
def save_data(user_list):
    print('These are your currently entered wishes:')
    print(user_list)
    if len(user_list) == 0:
        print('Skipping the creation of an empty file.')
        return None
    else:
        print('::: Save to the default file (wish_data.csv)? Type Y or N')
        user_choice = input('> ')
        if user_choice == 'Y':
            save_list_to_csv(user_list, 'wish_data.csv')
            print('Saving the database in wish_data.csv')
            print('Database contents:')
            print(user_list)
        else:
            print('::: Enter a file name to save to.')
            filename = input('> ')
            save_list_to_csv(user_list, filename)
            print(f'Saving the database in {filename}')
            print('Database contents:')
            print(user_list)

def save_list_to_csv(user_list, filename):
    fileline = ''
    with open(filename, 'w', newline = '') as file:
        max_index = (len(user_list)-1)
        for (index,entry) in enumerate(user_list):
            if index == max_index:
                fileline += f"{entry}\n"
            else:
                fileline += f"{entry},"
        file.writelines(fileline)
    return file
