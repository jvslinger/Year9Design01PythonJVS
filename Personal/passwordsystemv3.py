count = 4


#Function: A function is a small set of instructions that can be called upon. 
#The below function your wrote, but input("What is your name: ") is a function
#you are simply using. 
def chosen_pokemon():

    while True: 
        count
        if count == 1:
            print ("Maximum Number of Attempts Exceeded.")
            print (" ")
            break
        while count > 1:
            count -= 1
            f = open("helloworld.txt","r")
            content = f.read()
            print ("Please enter your password.")
            fav_type = raw_input()
            if content in fav_type:
                print ("Password Correct.")
                print (" ")
                print ("How are you today, my dear friend?")
            else:
                print (" ")
                print ("Sorry, password Incorrect.")
                print ("Attempts Remaining:")
                print (count - 1)
                print (" ")
                continue
            return 

chosen_pokemon()

#Phase 1: replace password with password reader, then put twice compare strings, "have program read file"
#Phase 2a: Find a way to enter the password into a file "have program create file"
#Phase 2b: Figure out a way to change password "have program replace file"
#Phase 3: Allow certain characters
#Phase 4: Demand certain characters
#Phase 5: Implement usernames into process somehow (username tells you which password to look for)
