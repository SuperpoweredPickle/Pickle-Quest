#intoduction
Name = input("Enter your name! ")
print(f"Greetings {Name} Welcome to your adventure! ")

start = input ("Would you rather play the game or perish >:( ")
if start == 'play':
    print ("Great! Let's play!")
    setting = input("Want to go to the Jungle, Desert or Tundra? ")
else:  
    print("Lame. Okay you're existence was wiped off the earth now")
    quit()
#jungle ending 1/3
if setting == "jungle":
    print ("Welcome to the mighty jungle! Your tour guide told you to wait here.... ")
    response = input("But he left to get ice-cream. Follow him or wait here? ") 
    
    if response == "Follow":
        print ("You follow him into the trees and stumble upon a family of gorillas. ")
        response = input("Do you fight them or back away or leave them be? ")
        if response =="fight":
                print ("You became their midday snack. ")
        elif response =="Leave them be":
            print ("They gave you a banana and accepted you in their family")
    elif response =="Wait":
        print ("You wait another 10mins and he still isn't here")
        #ending 1/3
    else:
        print ("Wrong answer, You lose. ")
        quit() 
if setting == "desert":
    print ("Welcome to the Sahara Desert! Your tour guide told you to wait here.... ")
    response = input("But he left to get ice-cream. Follow him or wait here? ")
    if response == "Follow":
     print ("You follow him into the dunes... ")
    elif response == "Wait":
        print ("You wait another 10mins and he still isn't here. ")
        #ending 1/3
    else:
        print ("Wrong answer, You lose. ")
        quit()
if setting == "tundra":
    print ('Welcome to the Tundra! Your tour guide turned into a human lolly! ')
    response = input ("Do you unfreeze him or abandon him? ")
    if response == "unfreeze":
            print ('He gave you 5 kebabs for your act of kindness :D ')
    elif response == "abandon":
            print ("He turned you into a kebab.")
#ending 3/3
