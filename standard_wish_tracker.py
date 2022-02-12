from genshin_wishes_functions import *

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
        print("Welcome to my personal genshin wish counter! (standard banner version)")
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
            user_list = data_entry()
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
            wish_stats(user_list)
        elif opt == "7":
            load_data(user_list)
        elif opt == "8":
            save_data(user_list)
        else:
            print('please enter a valid option from menu <3')
        print("Press Enter to continue to the menu.")
        print("Press Q to exit.")
        user_choice = input("> ")
        if (user_choice == "Q") or (user_choice == "q"):
            break
        else:
            continue
    print("Goodbye!")

# character banner pity recorder / calculator??
# 5 star character: guaranteed in 90 pulls
    # if last character was not event char:
        # next character probabiltiy of being event char is 100%
    # else: (last character was event char)
        # next character probabiltiy of being event char is 50%
# 4 star: guaranteed in 10 pulls
    # if last character was not 1 of 3 featured chars:
        # next character probability of being a featured char is 100%
    # else: (last character was a featured char)
        # next character probability of being event char is 50%
        # each 4 star has 50% chance of being 1 of the 3 featured chars
        # the chance distributed equally among chars
        # hence any 4 star pull has a 16.67% chance of being a particular char
