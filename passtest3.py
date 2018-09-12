count = 4
def chosen_pokemon():
    while True: 
        global count
        if count == 1:
            print "Maximum Number of Attempts Exceeded."
            print " "
            break
        while count > 1:
            count -= 1
            print "Please enter your password."
            fav_type = raw_input()
            if "shmoopy" in fav_type:
                print " "
                print "Password Correct."
                print " "
                print "Welcome to the secure server."
            else:
                print " "
                print "Sorry, password Incorrect."
                print "Attempts Remaining:"
                print count - 1
                print " "
                continue
            return 

chosen_pokemon()