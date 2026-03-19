#intoduction
Name = input("Enter your name! ")
print(f"Greetings {Name} Welcome to your adventure! ")

start = input ("Would you rather play the game or perish >:( ")
if start == 'play':
    print ("Great! Let's play!")
    setting = input("Want to go to the Jungle or Desert? ")
else:  
    print("Lame. Okay you're existence was wiped off the earth now")
    quit()
#jungle ending 1/3
if setting == "Jungle":
    print ("Welcome to the mighty jungle! Your tour guide told you to wait here.... ")
    response = input("But he left to get ice-cream. Follow him or wait here? ")
    if response == "Follow":
     print ("You follow him into the trees... ")
    elif response == "Wait":
        print ("You wait another 10mins and he still isn't here")
        #ending 1/3
    else:
        print ("Wrong answer, You lose. ")
        quit()
#tutorial used
#https://youtu.be/u8X6TiJA8as?t=663
