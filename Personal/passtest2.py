def chosen_pokemon():
    while True: 
        for trial in range(3):
            print "Please enter your password."
            fav_type = raw_input()
            if "davey" in fav_type:
                print "Password Correct."
            else:
                print "Sorry, password Incorrect."
                continue
        else:
            sys.exit(10)
            return 

chosen_pokemon()

#check count then at beginning

#if count = 0 then kill

#set count 3

#then do -1 count and read count at end