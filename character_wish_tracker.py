# import sys
# insert at position 1 in the path, as 0 is the path of this file.
# sys.path.insert(1, '/Users/trac.k.y/Documents/python coding fun/standard_wish_tracker.py')
# never mind i don't need that 
from genshin_wishes_functions import *

# option 1
def char_valid_stars(wish):
    if (wish == "3") or (wish == "4") or (wish == "4*") or (wish == "5") or (wish == "5*"):
        return True
    else:
        return False

def char_star_checker(wish):
    while True:
        if char_valid_stars(wish) == False:
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
        elif char_valid_stars(wish) == True:
            return True

def char_data_entry():
    print("Enter how many stars each of your wishes has, separated by a space:")
    print("Denote any banner four and five stars with an asterisk (4* or 5*)")
    user_input = input("> ")
    user_list = user_input.split()
    for (index,entry) in enumerate(user_list):
        if char_star_checker(entry) == True:
            user_list[index] = entry
    return user_list

# option 6 modified functions

def char_four_star_pity(user_list):
    user_pity = 0
    guarantee = False
    for (index,entry) in enumerate(user_list):
        if (entry == '4'):
            user_pity = 0
            guarantee = True
        elif entry == "4*":
            user_pity = 0
            guarantee = False
        else:
            user_pity += 1
        continue
    return [user_pity,guarantee]

def char_five_star_pity(user_list):
    user_pity = 0
    guarantee = False
    for (index,entry) in enumerate(user_list):
        if (entry == '5'):
            user_pity = 0
            guarantee = True
            continue
        elif (entry == '5*'):
            user_pity = 0
            guarantee = False
            continue
        else:
            user_pity += 1
            continue
    return [user_pity,guarantee]

def char_four_star_counter(user_list):
    four_stars = 0
    featured = 0
    for (index,entry) in enumerate(user_list):
        if (entry == '4'):
            four_stars += 1
        elif (entry=='4*'):
            four_stars += 1
            featured += 1
    return [four_stars,featured]

def char_five_star_counter(user_list):
    five_stars = 0
    featured = 0
    for entry in user_list:
        if (entry == '5'): 
            five_stars += 1
        elif (entry == '5*'):
            five_stars += 1
            featured += 1
    return [five_stars,featured]

def char_wish_stats(user_list):
    wish_total = total_wishes(user_list)
    four_star_total = char_four_star_counter(user_list)
    five_star_total = char_five_star_counter(user_list)
    user_4starpity = char_four_star_pity(user_list)[0]
    four_star_guarantee = char_four_star_pity(user_list)[1]
    user_5starpity = char_five_star_pity(user_list)[0]
    five_star_guarantee = char_five_star_pity(user_list)[1]
    print("You have made a grand total of",wish_total,"wishes.")
    print(f"({wish_total * 160} primogems)")
    print("You have pulled a total of",four_star_total[0],"four stars, and a total of",five_star_total[0],"five stars.")
    print("Of those",four_star_total[1],"have been featured four stars, and",five_star_total[1],"have been the featured five star.")
    print("You are at",user_4starpity,"four star pity, so you need",(10-user_4starpity),"more wishes to get your next guaranteed four-star.")
    if four_star_guarantee == True:
        print("Your next four star is guaranteed to be one of the three banner characters.")
    if user_4starpity >= 8:
        print("You are also around four-star soft pity, so you should get one very soon.")
    print("You are at",user_5starpity,"five star pity, so you need",(90-user_5starpity),"more wishes to get your next guaranteed five-star.")
    if user_5starpity >= 75:
        print("You are also around five-star soft pity, so you should get one very soon.")
    if five_star_guarantee == True:
        print("Your next five star is guaranteed to be the banner character.")
    elif five_star_guarantee == False:
        print("You have to win the 50/50 to get the banner character.")
    
    

if __name__ == "__main__":
    opt = None
    user_list = []
    my_menu = {"1": "Enter wishes",
               "2": "Display current wishes",
               "3": "Add wishes",
               "4": "Update wishes",
               "5": "Delete wishes",
               "6": "Wish statistics",
               "7": "Import data from csv",
               "8": "Export data to csv",
               "Q": "Quit program"}
    while True:
        print("Welcome to my personal genshin wish counter! (character banner version)")
        print_menu(my_menu)
        print("Choose an option:")
        opt = input("> ")
        if (opt == 'Q') or (opt == 'q'):
                print("Quitting the program!")
                break
        else:
            if check_option(opt, my_menu) == "invalid": 
                print("Do you wish to continue? (Y/N)")
                user_choice = input("> ")
                if user_choice == "Y":
                    continue
                else:
                    print("Quitting the program!")
                    break
            print("You selected option {}: {}.".format(opt, my_menu[opt]))

        if opt == '1':
            user_list = char_data_entry()
        elif opt == '2':
            if user_list == []:
                print("There are no wishes to display.")
            else:
                print("The rarities of your currently stored wishes are:")
                print(user_list)
        elif opt == '3':
            add_data(user_list)
        elif opt == '4':
            update_data(user_list)
        elif opt == "5":
            delete_data(user_list)
        elif opt == "6":
            char_wish_stats(user_list)
        elif opt == "7":
            load_data(user_list)
        elif opt == "8":
            save_data(user_list)
        else:
            print('please enter a valid option from menu <3')
        print("**********")
        print("Press Enter to continue to the menu.")
        print("Press Q to exit.")
        user_choice = input("> ")
        if (user_choice == "Q") or (user_choice == "q"):
            break
        else:
            continue
    print("Goodbye!")
