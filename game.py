rewards = ["kebabs", "banana", "knuckle sandwich"]

#intoduction
def introduction():
    Name = input("Enter your name! ")
    print(f"Greetings {Name} Welcome to your adventure! ")
introduction()

start = input ("Would you rather play the game or perish >:( ")
if start == 'Play':
    print ("Great! Let's play!")
    setting = input("Want to go to the Jungle, Desert or Tundra? ")
else:
    print("Lame. Okay you're existence was wiped off the earth now")
    quit()

if setting == "Jungle":
    print ("Welcome to the mighty jungle! Your tour guide told you to wait here.... ")
    response = input("But he left to get ice-cream. Follow him or wait here? ")

    if response == "Follow":
        print ("You follow him into the trees and stumble upon a family of gorillas. ")
        response = input("Do you fight them or back away or leave them be? ")
        if response =="fight":
                print ("You became their midday snack. ")
        elif response =="Leave them be":
            print ("They were thankful and accepted you in their family")
            print("Reward:" + rewards [1])
    elif response =="Wait":
        print ("You wait another 10mins and he still isn't here")
        #ending 1/3
    else:
        print ("Wrong answer, You lose. ")
        quit()

if setting == "Desert":
    print ("Welcome to the Sahara Desert! Your tour guide told you to wait here.... ")
    response = input("But he left to get ice-cream. Follow him or wait here? ")
    if response == "Follow":
        print ("You follow him into the dunes and see a child. ")
        response = input ("Do you give them a knuckle sandwich or the cheese touch? ")
        if input == "Give him the cheese touch":
            print ("he passed it on to your guide")
        elif input == "Give him a knuckle sandwich":
            print ("He gave you one back :D")
    elif response == "Wait":
        print ("You wait another 10mins and he still isn't here. ")
        #ending 1/3
    else:
        print ("Wrong answer, You lose. ")
        quit()

if setting == "Tundra":
    print ('Welcome to the Tundra! Your tour guide turned into a human lolly! ')
    response = input ("Do you unfreeze him or abandon him? ")
    if response == "Unfreeze him":
            print ('He was grateful for your act of kindness :D ')
            print ("Reward:" + rewards[0])
    elif response == "Abandon him":
            print ("He turned you into a kebab.")

#ending 3/3
