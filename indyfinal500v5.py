from ast import unparse
import time, sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  value = input()  
  return value
def fast_set2():
    answer=typingInput("\n\nYou approach the first corner, it's all very tense! \nHow do you wish to proceed? \n\n 1) Take it easy! \n 2) Like a leaf in the wind you breeze into the corner! \n 3) You fly into it like a bat out of hell!\n\n")
    if answer=="1":
        typingPrint("\n\nYou went too slow, you fell behind!\n")
        corn2()
    elif answer=="2":
        typingPrint("\n\nPerfectly executed, you are nailing this, and looking good doing it too!")
        corn2()
    elif answer=="3":
        game_over_crash()
    else:
        typingPrint("\n\nPlease enter the corresponding Number and try again")
        fast_set2()
def fast_set():
    typingPrint("\n\nYou get an excellent start, great job!")
    typingPrint("\n\nHowever, you can hear a car coming from behind") 
    answer=typingInput("\n\nHow do you wish to proceed?\n\n 1) Cut the other car off!\n 2) Let them stay behind you!\n\n")
    if answer=="1":
        typingPrint("\n\nExcellent move!") 
        typingPrint("\n\nYou cut them off and they go flying off the track.") 
        typingPrint("\n\nYou're still in the hunt to win this race!")
    elif answer=="2":
            game_over_crash()
    else:
        typingPrint("\nPlease enter the corresponding Number and try again\n")
        fast_set()
def slow_set():
    typingPrint("\n\nYou set off too slow, so many other cars pass you by, leaving you in their dust!")
    answer=typingInput("\n\nYou start drafting behind the car in front of you. \n\n What would you like to do? \n\n 1) Keep drafting! \n 2) Try to pull ahead!\n\n")
    if answer=="1":
        typingPrint("\n\nYou slingshot past the car in front of you, excellent work!")
    elif answer=="2":
        return game_over_crash()
    else:
        typingPrint("\n\nPlease enter the corresponding Number and try again")
        slow_set()
def slow_set2():
    answer=typingInput("\n\nYou approach the first corner, \nHow do you wish to proceed? \n\n 1) Take it easy! \n 2) Like a leaf in the wind you breeze into the corner! \n 3) You fly into it like a bat out of hell!\n\n")
    if answer=="1":
        typingPrint("\n\nYou went too slow, now you're at the end of the pack")
        corn2()
    elif answer=="2":
        typingPrint("\n\nPerfectly executed, you fly past the cars and take a lead. You're nearing the front of the pack")
        corn2()
    elif answer == "3":
        game_over_crash()
    else:
        typingPrint("\n\nPlease enter the corresponding Number and try again")
        slow_set2()
def wrong():
    answer=typingInput("\n\nThat's not a real answer, try either 'yes' or 'no'\n\n").capitalize()
    if answer=="Yes":
        typingPrint("\nWelcome back, let's run that again\n")
        start_race()
    elif answer=="No":
        typingPrint("Winners never quit, guess that makes you a loser")
        exit()
def start_race():
    time.sleep(1)
    typingPrint("\nWelcome to the Indy 500")
    typingPrint("\n\nThe lights are on and we're ready to go") 
    typingPrint("\n\n3...")
    time.sleep(1)
    typingPrint("\n\n2...")
    time.sleep(1)
    typingPrint("\n\n1...")
    time.sleep(1)
    typingPrint("\n\nGO!")
    answer=typingInput("\n\nHow would you like to proceed? \n\n 1) Drop into gear and go! \n 2) Hit the accelerator! \n 3) Floor it!\n")
    if answer=="1":
        slow_set()
        slow_set2()
    elif answer=="2":
        fast_set()
        fast_set2()
    elif answer=="3":
        game_over_crash()
    else:
        typingPrint("\n\nPlease enter the corresponding Number and try again")
        start_race()
def game_over_crash():
    typingPrint("\nThe car just hit you\n")
    typingPrint("\nYou crashed and burned\n\n")
    typingPrint("\n\nGame Over\n\n")
    answer=typingInput(f"\nWould you like to start again, {driver_name}?\n").capitalize()
    if answer=="Yes":
        typingPrint(f"\nWelcome back {driver_name}, let's run that again\n")
        start_race()
    elif answer=="No":
        typingPrint("\nWinners never quit, guess that makes you a loser\n")
        exit()
    else:
        answer=typingInput("\n\nThat's not a real answer, try either 'yes' or 'no'\n\n").capitalize()
        if answer=="Yes":
            typingPrint("\nWelcome back, let's run that again\n")
            start_race()
        elif answer=="No":
           typingPrint("Winners never quit, guess that makes you a loser")
           exit()
        else:
            wrong()

def game_over_explode():
    typingPrint("\n The car Exploded\n")
    typingPrint("\nYou burnt to death\n\n")
    typingPrint("\n\nGame Over\n\n")
    answer=typingInput(f"\nWould you like to start again, {driver_name}?\n").capitalize()
    if answer=="Yes":
        typingPrint(f"\nWelcome back {driver_name}, let's run that again\n")
        start_race()
    elif answer=="No":
        typingPrint("\nWinners never quit, guess that makes you a loser\n")
        exit()
    else:
        answer=typingInput("\n\nThat's not a real answer, try either 'yes' or 'no'\n\n").capitalize()
        if answer=="Yes":
            typingPrint("\nWelcome back, let's run that again\n")
            start_race()
        elif answer=="No":
           typingPrint("Winners never quit, guess that makes you a loser")
           exit()
        else:
            wrong()


def corn2():
    answer = typingInput("\n\n How do you wish to proceed? \n\n 1) Accelerate \n 2) Change gear \n 3) Overtake \n 4) Check mirrors \n\n")
    if answer=="1":
        acc1()
    elif answer=="2":
        acc2()
    elif answer=="3":
        typingPrint("\n\nYou tried to overtake before undertaking adequate preparation, racing is no joke. You are dead.\n\n")
        game_over_crash()
    elif answer=="4":
        acc3()
    else:
        typingPrint("\n\nPlease select the corresponding number and try again\n\n")
        corn2()

def mirrors4():
        answer2_mirrors = typingInput("\nNice gear change, but there is a driver preparing to overtake you, hurry up and make your move...\n\n How do you wish to proceed?\n\n 1) Accelerate \n 2) Overtake\n\n")
        if answer2_mirrors=="1":
            answer2_mirrors = typingInput("\nAcceleration in progress. You are now catching up to position 5 Only one thing left to do...\n\n 1) Overtake\n\n")
            if answer2_mirrors=="1":
                typingPrint("\nSmooth overtake, well done. You are now in fifth place.")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again\n")
                mirrors4()
        elif answer2_mirrors=="2":
            typingPrint("\n\nYou tried to overtake without accelerating and you spin off the track as your back wheel was clipped by the driver behind. \n\n")
            game_over_crash()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            mirrors4()
def gears4():
        answer2_gears = typingInput("\nAcceleration in progress. You are now catching up! .\n \nHow do you wish to proceed?\n\n 1) Change Gears \n 2) Overtake\n\n")
        if answer2_gears=="1":
            answer2_gears = typingInput("\n*Gear change in progress*\n\nNice work! Brace yourself for overtake...\n\n 1) Overtake\n\n")
            if answer2_gears=="1":
                typingPrint("Smooth overtake, well done. You are now fifth place.")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again")
                gears4()
        elif answer2_gears=="2": 
            typingPrint("\nDamn, you forgot to change gears. So close.\n\n")
            game_over_crash()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            gears4()
def acc3():
    answer1_acc = typingInput("\nNice mirror check. The coast is clear.\n\n How do you wish to proceed?\n\n 1) Accelerate \n 2) Change gears\n 3) Overtake\n\n")
    if answer1_acc=="1":
        gears4()
    elif answer1_acc=="2":
        mirrors4()
    elif answer1_acc=="3":
        typingPrint("\n\n*STALL*\n\nOops, the other racers left you in the dust\n\n")
        game_over_crash()
    else:
        typingPrint("\nPlease select the corresponding number and try again")
        acc3()
def mirrors3():
        answer2_mirrors = typingInput("\nThere is a driver preparing to overtake you, hurry up and make your move...\n\nHow do you wish to proceed?\n\n 1) Accelerate \n 2) Overtake\n\n")
        if answer2_mirrors=="1":
            answer2_mirrors = typingInput("\nAcceleration in progress. You are now catching up to position 5. Only one thing left to do...\n\n 1) Overtake\n\n")
            if answer2_mirrors=="1":
                typingPrint("\nSmooth overtake, well done. You are now in fifth place.")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again")
                mirrors3()
        elif answer2_mirrors=="2":
            typingPrint("\nYou tried to overtake without accelerating and you spin off the track as your back wheel was clipped by the driver behind.\n\n")
            game_over_crash()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            mirrors3()
def gears3():
        answer2_gears = typingInput("\nAcceleration in progress. You are now catching up to position 5.\n \nHow do you wish to proceed?\n\n 1) Overtake \n 2) Check mirrors\n\n")
        if answer2_gears=="1":
             typingPrint("\nYou failed to check your mirrors, colliding with the car approaching your back right tire. Please swiftly make your way to the hospital.\n\n")
             game_over_crash()
        elif answer2_gears=="2":
            answer3_mirrors = typingInput("\nSafety first. The road is clear. Only one thing left to do...\n\n 1) Overtake\n\n")
            if answer3_mirrors=="1":
                typingPrint("\n Fifth place stares over in awe as you swiftly leave him in the dust.\n\n You are now in position 5.")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again")
                gears3()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            gears3()
def acc2():
    answer1_acc = typingInput("\n\nWell done. You almost burnt out your clutch. Close call. How do you wish to proceed?\n\n 1) Accelerate \n 2) Overtake\n 3) Check mirrors\n\n")
    if answer1_acc=="1":
        gears3()
    elif answer1_acc=="2":
        typingPrint("\nYou tried to overtake without accelerating and you spin off the track as your back wheel was clipped by the driver behind\n\n")
        game_over_crash()
    elif answer1_acc=="3":
        mirrors3()
    else:
        typingPrint("\nPlease select the corresponding number and try again")
        acc2()
def mirrors2():
        answer2_mirrors = typingInput("\nSafety first. The road is clear. How do you wish to proceed?\n\n 1) Change gear\n 2) Overtake\n\n")
        if answer2_mirrors=="1":
            answer2_mirrors = typingInput("\nWell done. You almost burnt out your clutch. Close call. Only one thing left to do...\n\n 1) Overtake\n\n")
            if answer2_mirrors=="1":
                typingPrint("\nCongrats!")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again")
                mirrors2()
        elif answer2_mirrors=="2":
            typingPrint("\nYou failed to change gear and burnt out your clutch, how are you going to race with a broken car?\n\n")
            game_over_crash()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            mirrors2()
def gears2():
        answer2_gears = typingInput("\nWell done. You almost burnt out your clutch. Close call. How do you wish to proceed?\n\n 1) Overtake \n 2) Check mirrors\n\n")
        if answer2_gears=="1":
            typingPrint("\nYou failed to check your mirrors, colliding with the car approaching your back right tire. Please swiftly make your way to the hospital.\n\n")
            game_over_crash()
        elif answer2_gears=="2": 
            answer2_gears = typingInput("\nSafety first. The road is clear. Only one thing left to do...\n\n 1) Overtake\n\n")
            if answer2_gears=="1":
                typingPrint("Fifth place stares over in awe as you swiftly leave him in the dust.\n\nYou are now in position 5.")
                q1()
            else:
                typingPrint("\nPlease select the corresponding number and try again")
                gears2()
        else:
            typingPrint("\nPlease select the corresponding number and try again")
            gears2()
def acc1():
    answer1_acc = typingInput("\nAcceleration in progress. You are now catching up to position 5.\n \nHow do you wish to proceed?\n\n 1) Change gear \n 2) Overtake \n 3) Check mirrors \n\n")
    if answer1_acc=="1":
        gears2()
    elif answer1_acc=="2":
        typingPrint("You failed to change gear and burnt out your clutch, how are you going to race with a broken car?\n\n")
        game_over_crash()
    elif answer1_acc=="3":
        mirrors2()
    else:
        typingPrint("\nPlease select the corresponding number and try again")
        acc1()
def q1():
    print("\n\nloading.   Indy500")
    time.sleep(1)
    print("loading..  Indy500")
    time.sleep(1)
    print("loading... Indy500")
    time.sleep(2)
    print("")
    print("Indy500...ready")
    print("Indy500...run")
    print("")
    time.sleep(2)
    print("")
    print("")
    print("")
    print("                          WELCOME BACK SPORTS FANS")
    print("             HALFWAY AROUND THE TRACK, NOW INTO THE BONUS ROUND")
    print("")
    time.sleep(1)
    print("                          GET READY FOR QUESTION 1")
    time.sleep(3)
    print("")
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(2)
    print("")
    print("")
    print("     Question 1: In the 80's film 'Back To The Future', the piece of tech used to make time-travel possible was called the Flux capacitor?")
    print("")
    time.sleep(2)

    answer = input("                         True or False? ").capitalize()
    time.sleep(1)
    A = "True"
    B= "False"
    if answer==A: 
        print("")
        print("")
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@@@@  _________________________________________________________ @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@@@@@@@@@@|")
        print("             |@@@@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@@@@@@@@@@|")
        print("             |@@@@@@@__________________________________________________________@@@@@@@@@@@@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        time.sleep(1)
        print(".")
        print("                                              CORRECT")
        print("                          New ability added = MIND CONTROL\n\n")
        q2()
    if answer==B:
        print("")
        time.sleep(1) 
        print(" ")
        print("                                     INCORRECT - THE ANSWER IS TRUE")
        print("                             |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$        $$       |")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                             |$$$$       $$$   $$$         $$$  $$       |")
        print("                             |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                                             TRY AGAIN FOR BONUS")
        time.sleep(2)
        q2()
    else:
        typingPrint('\n\nPlease type "True" or "False\n\n')
        q1()
def q2(): 
    print("                                        QUESTION 2 IS COMING UP.........")

    time.sleep(1)
    print("loading.")
    time.sleep(1)
    print("loading..")
    time.sleep(1)
    print("loading...")
    time.sleep(2)
    print("")


    print("     Question 2: The Flux capacitor needed 2.21 gigawatts of electrical power to function?")
    print("")
    time.sleep(1)
    answer = input("                         True or False? ").capitalize()
    print(" ")
    A = "True"
    B= "False"
    if answer==A:
        print(" ")
        time.sleep(1)
        print("                       INCORRECT")
        print("                       THE ANSWER IS FALSE, IT NEEDS 1.21 GIGAWATTS OF ELECTRICITY")
        print("")
        print("                             |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$        $$       |")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                             |$$$$       $$$   $$$         $$$  $$       |")
        print("                             |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("")
        time.sleep(2)
        q3()
    if answer==B:
        print(" ")
        print(" ")
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@ _________________________________________________________  @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@|")
        print("             |@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@|")
        print("             |@@@ __________________________________________________________ @@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        print(" ")
        print("                           CORRECT...SUPER TYRES ADDED TO VEHICLE")
        time.sleep(2)
        q3()
        print("")
        print("")
    else:
        typingPrint('\n\nPlease type "True" or "False\n\n')
        q2()
def q3():
    print("                                     Question 3 is coming up -")

    time.sleep(1)
    print("")
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(2)

    print("")
    print("")
    print("     Question 3 - The train in the children's film The Polar Express is powered by a flux capacitor?")
    print("")
    time.sleep(1)
    answer = input("                         True or False? ").capitalize()
    print("")
    time.sleep(1)
    A = "True"
    B= "False"
    if answer==A:
        print(" ")
        print(" ")
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@  _________________________________________________________ @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@|")
        print("             |@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@|")
        print("             |@@@ __________________________________________________________ @@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        print(" ")
        print("                              CORRECT - MINES added to inventory")
        time.sleep(2)
        print(" ")
        print(" ")
        q4()
    if answer==B:
        print(" ")
        time.sleep(1)
        print("                                 INCORRECT, THE ANSWER IS TRUE")
        print("             It can be seen in the engine room scene aboard the Christmas train")
        print("                             |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$        $$       |")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                             |$$$$       $$$   $$$         $$$  $$       |")
        print("                             |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("")                                       
        print("")
        time.sleep(2)
        q4()
    else:
        typingPrint('\n\nPlease type "True" or "False\n\n')
        q3()
def q4():
    print("                                        QUESTION 4 COMING UP") 
    
    print("")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(2)

    print("")
    print("")
    print("     Question 4 - Nintendo is over 130 years old?")
    time.sleep(1)
    answer = input("                         True or False? ").capitalize()
    print("")
    A = "True"
    B= "False"
    if answer==A:
        print(" ")
        print(" ")
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@  _________________________________________________________ @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@|")
        print("             |@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@|")
        print("             |@@@ __________________________________________________________ @@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        time.sleep(1)
        print("                     CORRECT, it was founded in 1889 by The Legend - Fusajiro Yamauchi-")
        print("                                     AIR SUPPORT added to inventory")
        time.sleep(2)
        q5()
    if answer==B:
        time.sleep(1)
        print(" ")
        print("                         INCORRECT, THE ANSWER IS TRUE")
        print("         It was founded in 1889 by The Legend - Fusajiro Yamauchi-")
        print("")
        print("                       |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                       |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                       |$$$$       $$$   $$$   $$$        $$       |")
        print("                       |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                       |$$$$       $$$   $$$         $$$  $$       |")
        print("                       |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                       |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("")
        time.sleep(2)
        q5()
    else:
        typingPrint('\n\nPlease type "True" or "False\n\n')
        q4()
def q5():
    print("")
    print("                             QUESTION 5 COMING UP")
    print("")
    print("")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(2)

    print("")
    print("")
    print("     Question 5 - The Flux capacitor was originally invented by Nikola Tesla")
    time.sleep(1)
    answer = input("                         True or False? ").capitalize()
    print("")
    A = "True"
    B = "False"
    if answer==A: 
        time.sleep(1)
        print("                                 INCORRECT, THE ANSWER IS FALSE") 
        print("                        Did you know Gullible has been removed from the English dictionary")
        print("")
        print("                             |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$        $$       |")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                             |$$$$       $$$   $$$         $$$  $$       |")
        print("                             |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                                 ENGINE DIAGNOSTICS - OIL LEAK DETECTED \n\n")
        time.sleep(2)
        q6()
    if answer==B:

        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@@  _________________________________________________________ @@@|")
        print("             |@@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@|")
        print("             |@@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@|")
        print("             |@@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@|")
        print("             |@@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@|")
        print("             |@@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@|")
        print("             |@@@@ __________________________________________________________ @@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        time.sleep(1)
        print("                       CORRECT!\n")
        print("                       Rewarded =  Engine upgrade.9.0\n\n")
        time.sleep(2)
        q6()
    else:
        typingPrint('\n\n             Please type "True" or "False\n\n')
        q5()
def q6():
    print("                                     QUESTION 6 COMING UP.........")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(2)
    print("     Question 6 - Guido Van Rossum the inventor of Python language, took the name 'Python' from the 'BBC hit series Monty Python's Flying Circus'")
    time.sleep(1)
    answer = input("                         True or False? ").capitalize()
    print("")
    A = "True"
    B= "False"

    if answer==A:
        print("")
        print("CORRECT - THE ANSWER IS TRUE - Guido van Rossum happened to be reading the completed manuscripts of Monty Python at the time")
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")                                
        print("             |@@@  _________________________________________________________ @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@@    @@|  |@@|  |@@|  |@@@|     @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@@@   @@|  |@@|  |@@|  |@@|      @@@|")
        print("             |@@@ |@@@@@@|    |@@@  @@@|  |@@ @@  @@|  |@@|  |@@|  |@@@@@@@| @@@|")
        print("             |@@@ |@@@  @@@|  |@@@  @@@|  |@@  @@ @@|  |@@|  |@@|       |@@| @@@|")
        print("             |@@@ |@@@  @@@|   |@@@@@@|   |@@    @@@|  |@@|  |@@|      |@@@| @@@|")
        print("             |@@@ |@@@@@@@|     |@@@@|    |@@     @@|  |@@@@@@@@|  |@@@@@@@| @@@|")
        print("             |@@@ __________________________________________________________ @@@|") 
        print("             |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|")
        time.sleep(1)
        print("                         Rewarded = BOOSTER PACK x5")
        print("")
        print("")
        print("                                             BONUS ROUND OVER")
        print("")
        print("                             EXIT THE PITSTOP, GET BACK IN THE RACE AND GOOD LUCK")
        print("disconnecting from bonus in 3...")
        time.sleep(1)
        print("disconnecting from bonus in 2..")
        time.sleep(1)
        print("disconnecting from bonus in 1.")
        time.sleep(1)
        fifth_place()
    if answer==B: 
        time.sleep(1)
        print("                                            INCORRECT")
        print("THE ANSWER IS TRUE - Guido van Rossum needed a short and catchy name and happen to be reading the completed manuscripts of Monty Python at the time, ")
        print("")
        print("                             |$$$$       $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$       $$$   $$$   $$$        $$       |")
        print("                             |$$$$       $$$   $$$   $$$$$$$$$  $$$$$$$$ |")
        print("                             |$$$$       $$$   $$$         $$$  $$       |")
        print("                             |$$$$$$$$$  $$$   $$$   $$$$$$$$$  $$$$$$$$$|")
        print("                             |$$$$$$$$$  $$$$$$$$$   $$$$$$$$$  $$$$$$$$$|")
        print("")
        print("                                      POWER LEVEL RUNNING AT 50%")
        print("")
        print("")
        print("                                             BONUS ROUND OVER")
        print("")
        print("                             EXIT THE PITSTOP, GET BACK IN THE RACE AND GOOD LUCK")
        print("disconnecting from bonus in 3...")
        time.sleep(1)
        print("disconnecting from bonus in 2..")
        time.sleep(1)
        print("disconnecting from bonus in 1.")
        time.sleep(1)
        fifth_place()
    else:
        typingPrint('\n\nPlease type "True" or "False\n\n')
        q6()
    time.sleep(1)

def restart():
    replay = typingInput("\n\nWould you like to play again, Yes or No?\n\n").capitalize()
    if replay == "Yes":
        start_race()
    if replay == "No":
        exit()
    else:
        typingPrint('Please type "Yes" or "No"')
        restart()
def third():
    typingPrint(f"\n\nYou just about finished 3rd {driver_name}, your prize is A practical guide on how to drive for beginners, Hope you enjoy!\n\n")
    prize3()
    time.sleep(5)
    restart()
def second():
    typingPrint(f"\n\nCongrats {driver_name}, You finished 2nd\n\nYour prize is a Brand new Golf GTI with a custom tuned modkit, Hope you enjoy!\n\n")
    prize2()
    time.sleep(5)
    restart()
def first():
    typingPrint(f"\n\nCongrats {driver_name}, You finished 1st...\n\n You just won a brand new Bugatti La Voiture Noire, we hope you enjoy it!\n\n")
    prize1()
    time.sleep(5)
    restart()
def fifth_place():
    step1()

def step1():
    typingPrint("\n\nYou are approaching the final corner, cars 3,7,9 and 10 are ahead\n\n")
    answer = typingInput("\nWhat do you want to do?\n\n 1) Use your mind control powers and force them to slow down?\n 2) Activate the land mine that you set onto the track?\n 3) Go into 6th gear?\n 4) Go down into the 4th gear?\n\n")
    if answer == "1":
        typingPrint("\n\nYou accidentally slowed them down too much and crashed\n\n")
        game_over_crash()
    elif answer == "2":
        step2()
    elif answer == "3":
        game_over_crash()
    elif answer == "4":
        step3()
    else:
        typingPrint("\nPlease select the corresponding number and try again...\n\n")
        step1()

def step2():
        answer = typingInput("\n\nIt Worked!, you are racing ahead, but you need to slow down so you don't crash into the wall ,do you want to...\n\n 1) Go down into 4th gear and make the turn\n 2) BRAKE!!!\n 3) Do nothing and make the turn\n\n")
        if answer == "1":
            step1in2()
        elif answer == "2":
            game_over_crash()
        elif answer == "3":
            step2in2()
        else:
            typingPrint("\nPlease select the corresponding number and try again...\n")
            step2()

def step1of1in2():
                answer = typingInput("You slowed him down alright, but the others have now caught up, what will you do?\n\n 1) Go into 6th Gear?\n 2) Stay in the 5th Gear?\n\n")
                if answer == "1":
                    second()
                elif answer == "2":
                    first()
                else:
                    typingPrint("\nPlease select the corresponding number and try again...\n")
                    step1of1in2()

def step1in2():
            answer = typingInput("You did it but car 9 is now racing ahead... What will you do?\n\n 1) Use your mind control to slow him down, then shift into 5th gear?\n 2) Request air support?\n 3) Crash into him?\n\n")
            if answer == "1":
                step1of1in2()
            elif answer == "2":
                step2of1in2()
            elif answer == "3":
                game_over_crash()
            else:
                typingPrint("\nPlease select the corresponding number and try again...\n")
                step1in2

def step2of1in2():
                answer = typingInput("\n\nBOOOM!!!, you were sent flying towards the racing line, you're only 20 yards away from victory, but now your car is in flames!!!, What will you do?\n\n 1) Stay in the car and drive towards the racing line\n 2) Leave the car and run Towards the Racing line\n 3) Swell the flames with water,then jump back into the car and claim victory!\n\n")
                if answer == "1":
                    game_over_explode()
                elif answer == "2":
                    first()
                elif answer == "3":
                    second()
                else:
                    typingPrint("\nPlease select the corresponding number and try again...\n")
                    step2of1in2()

def step2in2():
            answer = typingInput("\nYou swapped paint with car 7, and slowed down drastically... What will you do?...\n\n 1) Use your mind control to slow him down, then shift into 5th gear?\n 2) Request air support?\n 3) Crash into him?\n\n")
            if answer == "1":
                answer = typingInput("You slowed him down alright, but the others have now caught up, what will you do?\n\n 1) Go into 6th Gear?\n 2) Stay in the 5th Gear?\n\n")
                if answer == "1":
                    third()
                elif answer == "2":
                    second()
            elif answer == "2":
                answer = typingInput("BOOOM!!!, you were sent flying towards the racing line, you're only 20 yards away from victory, but now your car is in flames!!!, What will you do?\n\n 1) Stay in the car and drive towards the racing line\n 2) Leave the car and run Towards the Racing line\n 3) Swell the flames with water,then jump back into the car and claim victory!\n\n")
                if answer == "1":
                    game_over_explode()
                elif answer == "2":
                    second()
                elif answer == "3":
                    third()
            elif answer == "3":
                game_over_crash()
            else:
                typingPrint("\nPlease select the corresponding number and try again...\n")
                step2in2()

def step3():
        answer = typingInput("You swapped paint with car 7, and slowed down drastically... What will you do?\n\n 1) Use your mind control to slow him down, then shift into 5th gear?\n 2) Request air support?\n 3) Crash into him?\n\n")
        if answer == "1":
            step1in3()
        elif answer == "2":
            step2in3()
        elif answer == "3":
            game_over_crash()
        else:
            typingPrint("\nPlease select the corresponding number and try again...\n")
            step3()


def step1in3():
            answer = typingInput("You slowed him down alright, but the others have now caught up, what will you do?\n\n 1) Go into 6th Gear?\n 2) Stay in the 5th Gear?\n\n")
            if answer == "1":
                 third()
            elif answer == "2":
                second()
            else:
                typingPrint("\nPlease select the corresponding number and try again...\n")
                step1in3()

def step2in3():
            answer = typingInput("\nBOOOM!!!, you were sent flying towards the racing line, you're only 20 yards away from victory, but now your car is in flames!!!, What will you do?\n\n 1) Stay in the car and drive towards the racing line\n 2) Leave the car and run Towards the Racing line\n 3) Swell the flames with water,then jump back into the car and claim victory!\n\n")
            if answer == "1":
                game_over_explode()
            elif answer == "2":
                second()
            elif answer == "3":
                third()
            else:
                typingPrint("\nPlease select the corresponding number and try again...\n")
                step2in3()
def prize1():
    print("""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%&(&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%@*#(((#&&&&%%%%#((#%&&&#(*,,.,,,,,.,,,..........   ,**/(### (##%%&@@@@%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*  .,(%&&&&&@.  @&&&&&%%%#*,,,,%*/*..****,.  .....%    ..*. ,*%(#*      *%%%&&@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   ,/%&&&&@ .  /&&&&&&&&&%%%%%%%%/,...........  ..../ ... *,,,,*  *&&%,/      /#%##&##%&@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(*,  &&&&,   *#&&&&@./,   &&&&&&&&&&&&&&&&&&%/,... ...,.    ....  (,,,**&.,,,,, .,*,,,*     *###((///***,,,,,,,,,**/(#@%&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@%(/*,***//(#%&@@@/  ,,,.  ,/%&&&&/, , ., **************/((#%%&.,...       .,,*///(/,/((#&@@@@#.////(((##%& .. (%%#((//**,,,,,,,,*//(((  .&&@%&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%,*,,,,,,,,,*(&(,((@*......... . ,%%/*, .*/((((((##%%%%#%#%%%%(,,,,**/#%%%%%###(((//////////(..(***///**//////(((((##%%. ##&%%##((///******//(//,,. ..... &&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*,,,,,..,,,(%,**(.,,,/,*&@%#&&#*#(.*(////*//***************,.,*.*###((////(##%&&%%##((((((((/(/.,,,*/////((((((((////*///(#,,,.,,.&%###((((((((((%., .....   ..&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&#*/,.....,(&&.,(,,#  ../#%&%*(#,*,.,/,****,***,*****/*..,/,..*,//(#%(&,*...,*,***,,,/%%%%#########*,,,*,(////*******/(%#*  .........,.,,,,*%###(((((##...#* .  ,.  ./%&&&&%&&&&&
%%%%%%%%%%%%%%%%%%%%%%.@....,(#%&.,#,.@&%%##&(/#(((((///*****,,,,,,**..,,/###@,,*.**,**#(%(%@&@..,,,*((((#((####%,%##%##(//***,,,*/(*  ............. .................,,...,,.,.(*    ,. , . %%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%@@.,,#&%%&,(,.@%%##&*(((////******,,,,,,/,...,*(#((((@*,,.*,,,/****(%%@*,,,,**/(#  .......   /%##((/*. .......... .....................,............,,,,..,.* *   / ./ . %%%%%%%%%%%
%%%%%%%%%%%%%%%%%%.../@&%%#%//%%##((///****,,,,,,,,,,(,....,*********(@.,./&%/.,   .    **,****//,  .,/  ,.... ,*   ................................... .......................  ,.  *  *(.  #%%%%%%%%%%
#################%&@&&%%#&@@%#(//***,,,,,,,,,,,/,,....,*,,,********#,,,*.   .,*,,,,,,,,,,*,*,*/  ..(*/  ..*  .. , *  ...........................................,............,  /..#    //..,###########
##################.@&%%@%         /,,,.././.....,,,,,,,,*****,*,,,,,,,,,,,,,,.,(*,       ...... ,*/*.       .,.  .*. ............  .       ...........  .....,..............., /  ,*,**(&. ,############
##################. *@#      ,,#(,  /.......,,,,,,*,*****,,///*  ..&.     ..........,,,,..... .,  , ,,    . .*    / . ...........        . ................................. . * . .    ..(*############
((((((((((((((((((,  .    ..., . . . */*,.                             ........,............. ,. *..,.  , . /.   .(  .................. .. .............................. .    *,,,  ,,.,**(((((((((((((
(((((((((((((((((((  .... ,.,.. .. .../...    ..,,/,,.         .  *    ........,............ ,,   .,    ,*/**.* ./,  . .....................,(&@@%%%%%%%%%%%%%&@(.            .  .   ,, ,.,****/////((((
((((((((((((((((((// ..... .. . , . . .......  . .. , ., ,.., ,, ,*....  ..................  ..  .,  ,.,,., . . ,(,* , ..*..../%&%###(((((/((((((((###%#,                      . .  ..*....,,,***///////
//////////////////#  .... . ..., ...  ....... . .  ... ,.  . . ,, *. . .    ...............  ,..,.    *.  %####(.   /, ......./*,,,,,,,,,***#(.                                     ......,,,***////////
/////////////////.,##.,... .. . . , ........      . .       .. .    .   &@#   ............  ...*,.   , .# .,#*     *,....... %#(/,*,                                              ..,,*/////////////////
//////////////,....,#....... . . .   *,..*/**   .. .  .  .    .  ., .          (//*,.. ...     .,,,#*,... %,..  ./,#, ..*.  .                                           ..,,*///////////////////////////
////////***///   .,&........ .   . *.......(***         ..  .  .....,.,,,. ,&.............    .,*,, . ... .,%##%.  .                                         ..,,*//**/**/*****//********///**/**///////
******************* ,,............/..*@*......,..,,..,..,,.,,.,,.,.......**//(#%&&&%(*****(            .    ,  .*,.                               ..,,**************************************************
**************,,,,,......                     .     ...............  .***,.                      . ..   *  ./* ,.                      ...,*************************************************************
***************,,,,,,,,......                                                                        ....,,,,..             ...,,***********************************************************************
*************************,,,,,,,.......                                                                          ..,************************************************************************************
*************************************,,,,,,.......                                              .,******************************************************************************************************
************************************************,,,,,,,,,,,,,,,,,,,,,,,*********************************************************************************************************************************
""")
def prize2():
    print("""
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ################################################(((//////***/************//(//**,.,.,,..,,,..,,,,,,,*****//(((##%%%%%%%%#%%%%%##%####################################(((((((((((((((((((((((((((((((((((
    #########################################(///***/(###((((((/*/,((///////////*,////*.,,,,,,........,,,,,,,*****//((((/**,*(#%%%%%%%%%%%%%%%%#############################((((((((((((((((((((((((((((((((
    ############################%#%#%#((((((.,///((((((((((((//*/,///////**********,,/***,****.,,,,,........,,,,,***////(((##((/* *#%%%##%%%%%#%%%%%#############################(((((((((((((((((((((((((((
    #############################%%,(((((/.*****////////******,*,,******,,,,,,,,,,,,,,,*/**,,///**,,,,,,,,......,**/////((((((#####(/,./%%%%%%%%%%%%%#################################((((((((((((((((((((((
    #############################(/((((/..,,,,,,,,,,,,,,,,,,,....,,,**,,,...,,...........*//**,////***,,,,,.......,****////((((########(*../#%%%%%##%%%%%###############################(##(((((((((((((((((
    #############################(((((..,.....,,,,,,.,,,,,..........*,....,/(((//((/. ... ,,(***./**/******,,,,....,*****/////(((####%#%%##(*. /#%%%%%%%%%%#####################################((((((((((((
    ############################(((((,........,............. .....,......(/,,,***,**,*. . ,,.*////***,,,,,,,,,,,....,,,.,.,,,***//((###%%%%%##(/.../%%%%%%%%##########################################((((((
    ######################%%###((((((*//////////////////////**********,,,,,.     ... ,*.     ..///////////////////(((/((////(((((((((((///((((///**...,(%%%%###########################################(((((
    #################%##%%##(((((((((((((((((((((((((((((((((((((((((((((((((((//*/*...,/(//((/((((((///////////////////////(((#((//(((((((((((((#####((#######(((#######################################(((
    #################%%(*(((#####(##(////*(##################(/(//((((((((((((((((((**/////(((((((((((((((((((((((/////////////***//((((////(((((((((((((((((((((((####((################################(((
    ################%#%/(#(((///(((((#######################((((###########(((((((((((((((#(****#((((((((((((((((//////////***************///////////////((((((((((((((((((((##(##########################((
    ################%##(########(###%%%%%%%%%%%%%%%%%%&&&%%&&&&&&&&&&&&%%%%%%%%%%%%##############(///////////(#(#(////*((((/**,,....,,,*******//*//////////////(((((((((((((((((((((%#######################
    #######################/,,,,,*(%/*******************************///((((######%%%%%%&&&&&&&&(*//*,     .*////%######/*/..(//.,      ,,//((##%/*#(((/*,,,,,,,,,,.(/(/*****//////(/*/######################
    ################%/*##,,,,    **,*******************************************************/////,       **/** ,///########*/* ,    .%&%*.   .. /%,,,....       .  ,((/,(.,,,.      ,.*(#####################
    #################*,,*.    ,**...************************************************,**********    ,//**.***(****///(((((((((//*,*,,,***,**,*,*,**********////////*,/(/#(//((((/((/#(#/(####################
    ###############%%**,   ***/((**, ,********,****************,,,,,,,,,,,,,,,,,****,********,   /,*/, /*/  /((***/*//(////(////*,,,,,,,,,,,,,,,,,**/////(((((/#(#########(#((#((((((##(/(##################
    ###############%#,,. ,*/./# #.(// ,**,,,,,,,,,,,*****,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,*,,***  ,*/. , .**  /    (*,**////////*.,,*/*,,,,,,,,,,,,,,,,,*******//(##(&((@@%@%/&&#%(@//*****/*(#################
    ############%%%%#,, ,/(  *.*   /*, ,*,,,,,******,***************,,,,,,,,,,,,,,,,,,,,,,**. ,,*, *   * ./  *%/#&,***///***,../**..  ..,.... .,..  .,,,**,***/%@&%&&&&&%%&@%#((%*/*****,,,(################
    ############%%%%/.. ,* * ,*,.##%&* .,,*,,,,********************************,,,,,,,,,,,,, .,.(.  ( ./*,.*/((##%#*******...,**,.#%&&*...(##%,,....,,,  ,,.   .    .. ..    ....,. *,*,,,,##############(((
    #########%%%%%%%#.,../* /.(/((,. / ..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,, ,,/,,(. ,,./(//*.. .  /****,...***. ....*#&#( .  ....        ..  .    ......   .....  ...,,,*(############(((((
    #########%%%%%%%%.,.*.,/#%/(#. .**. ,,,,,*/////////****,,,......................,,,,,.., ,*. .  ./(,/(.(  , /%#*,,,,  .,,,,, *#(.  ..,%%/.,...    .....    ...,.     ...,   ....  .*#*#############(((((
    ########%%%%%%%%%%#(*...*/(* / ./,. ,*********////**/*****/********//*//*///*/*/*****,,,,,,, .   /(*(./ ., .. (,//**,,,   ....,,,,,,,,,,,,,,,,******************,*****/**,,,,,,,..,,*/####(########(((((
    #######%%%%%%%%%%%%%,//. /.,*,*(*..         .,*/%%%/*****,..                             .,*(*,.  ,*../  */. *..////////***,,,,,,,,......                            .............. ,(###############(((
    %%%%%%%%%%%%%%%%%%%%%*//,* ,*.(,,,.      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(      . ./      .,** ,%.*  ## ##.(#,.             .........                                        .(%########################
    #########((###########**#*,/%*.,...    ,##(((((((((((((((((((((((((((((((((,   .           *,,* (,    #../*,....     (########((##################%#%,      ,,        .....*##############(######(((((((
    #######(((///******,,,.,.. ...       .,.,,,................................,..          ,*****,,,*******,,.....   .((#((###############################*              ..,/%#%###########################
    ###########################################################################((((((((((///////************,,,,,,,,,,.........                                                          ...,,,,,***////////
    """)
def prize3():
    print("""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%##%%%###%%%#%%%%%%%%%%%%%%%###%####%%#%%##%#%%%#%%%%%##%#%##%%##%%%%%%%%%#%%%%%%%%##%#%%##%%%%#%#%%%%%##%#%%%%%%#%#%%%##%#%#%#%##%%%%%##%%%%%##%%%%%##%%%%%##%##%%%#%%%#%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%#%..    /.*###%%%###%%%%%%##.   /#%.     %     *# ,%%#. . (# *%%%. .%### *%#%%%%%(    ,##  #%#%  #/    (%%(   %#%%%###( .  *#* (%#( *%. (#     #%#      %%%#%##%%%%%##%%%%%%%%%%%#%%%%%%%
#%#%#%%%%%%%%%####%/.%%%,*/,*%#%(,*(%##%%( *%%% .%, (%#%#  %#### ,%, (%%#%# ,%#, (  %## ,%%##%%%( ,%%, (( ,%%,.#/ ,%%%#%%..# /%##%##  ####%%, (%%( *#. (# .#%/ *%  #%#%##%%* ,/%(*,/%%%%%%%%%%%%%%%%%###
#%#%###############/.%#%,*#%*,#,*%%/,%###* /%#%. #, .,,/#  .,*## .%  %%#### ,%# *%( *%# ,%%#####( ,#%* *%, (( *###/  ./#, (%. (####( ,%,  .%* (#%( *#. (# .%## .%  ,,,/%###% /%*,#%# ###################
##################%/.%#%./#%*,%*,%#%%####% ,##/ ,%, (####  ##%## ,#* ,%#### *%  ***  (( ,%######/ ,%%. ##%. ..%#####( ,# .**/  %###%. /%% .%* /#%* *#. (# .%%. /#  #%##%###% (#*,%#( ###################
###################((###((##((###(//#####%#((/(%##(/#####//#####/(##%((/(##/((/#####//#*////#####////##%###//####(///##(/####(/(###%##(//(####(//(###(/##////(###//////######/(##(((####################
##############################################################################################################################################################%%########################################
#################////(###########//////////////(#########//////##########(//////////(##%######(/////(#######%////###%(////####(/////(########////##########(/*,,,,*/(###################################
#################....,##########/..............*#######(........(########,.............,.#####,......,#######..../##%,..../###.......*######/....(######.,.,....,,,....#################################
#################....,##########/....*#################,...**....%#######,....#####(,.,...####,...,,..,######..../###,..../###..,.,..,*#####/....(####.,..,,(######(,*##################################
#################....,##########/....*################*....#(....,#######,....#######*,.../###,...,,....####(..../###,..../###....*...,*####/....(###.....(#############################################
#################....,##########/....*###############(....*##/..../######,....######(.,,,.%###,...,#....,###(..../###,..../###...,*/.,..*###/....(##,..../##############################################
#################....,##########/.....,,.......######..,.,####.....(#####,....,.,..,....(#####,....##,.,.,###..../###,..../###..,.,#(....*##/....(#(.....####(,........#################################
#################....,##########/.....,,,,,,,,*#####*....(####(...,,#####,.......,....*#######,...,##(.,.,,##..../###,..../###....*##/..,,*#/....(#(....,####(.........#################################
#################....,##########/....*#############/..........,.....*####,....(####,..,.*#####,...,###(....,(..../###,..../###....*###/.,..*/....(##.....(########,....#################################
#################....,##########/....*#############,................./###,,...######*..,.,####,...,#####....*,.../###,..../###....,####(.,.,(..,.(##/.....########,....#################################
(################....,##########/....*############,....*########/....,###,....#######*.,..,###,...,######.,....../###,..../###....,#####(.,.,....(###,.....*######,....#################################
(###############(...........,,*#/..............*#(.....##########,.....##,....(#######,....,(#,...,######(......./###,..../###....,######(.......(####(,.,...........,.#################################
(###########(####............./#(..............*#,....(##########(,..../#*....(#######(,..../(/...,#######(....../###*....(#(#,...*#######/......#########/,...,....,(##################################
(##################################(###########(###(#############((##########(###(##############((#########(######((##(####((#####(#####################################################################
(#############((#############(##(((##((#(######(#######((#(###########(#################(##############################################((######################((##################(####################
(#########(###(#(..........,#,...,,.,.(#((((((#,,.,...,./##/.........(##,.,(/...(###(/..*(,,,.,....(###############################################################################(####################
(###################(..,##(#,..(#((#,..(#######,..(###*..*(/..*###(..,(#,.,/#*,.*(#((...((,..(#(((########################################################################(/*.    *##((#########(####(#(
(#########(((((((((((..,##((..,(((#(/..*#(((((#,..(((#(..,#/..,//,..,((#,..(((,..((#*..(((,..,,..,*(##########################################################%%(,.                (##((((((((((((((((((
(#(#(((((((((((((((((..,#(((.,,((((#/..*#(((((#,..(((#(...#/..,/*.,.(((#,../#((..,#(..*#((,..(##((#(############################(########(((((####((####.                          ,#(((((((((((((((((((
(((((((((((((((((((((..,#((#,../((((*../((((((#,..#(##*..,(/.,*(((,..*##,..(##(/../,.,(#((,..((((((((###########################(########((((((((((((#(##         ..**              /#((((((((((((((((((
(((((((((((((((((((((..,#((((,...,,.,./(((((((#,...,..,.*((/..*((#(,,./#*..(####*....(((((,.......,#((((((((((((((((((((((((((((((((((((((((((((((((((#(#,      /(#((#.             .##(((((((((((((((((
((((((((((((((((((((#(((#(((((#((/(((((((((((((((((((((((((#(((((((#((###(####((#((((((((((((((((((#((((((((((((((((((((((((((((((((((((((((((((((((((((#%.     .#(##((              *##(#((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#####################((((((((((#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((#/      *##(##*     .,.      ##((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((####(#((###################(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#,      (#############.     .#((((((((((((((((
((((((((((((((((((((#((((((((#((((((((#(((((((((((((((((((####((#####################(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#(      ,#############/      (#(((((((((((((((
((((((((((((((((##.#.//#(/((((/((*/(/*,,(*((/*,.(#.*/((*##*((,((#(.(//###,*(#*(#*((/#(/(///*#/(*(((/*(/*(//((*((*/(/*(*((((((((((((((((((((((((((((((((((((#/      (###(/,.            .##((((((((((((((
((((((((((((((((((,#,(,*.(((/.#,*///,(,*.//**(/*((.(*/,#*.%,/..##(.///*##,#,*/((**/./#(.,(*(/,# (#/*/*.(**/(,(,,/,/.#./((((((((((((((((((((((((((((((((((((##                        .,*((((((((((((((((
(((((((((((((((((((((((((#(((.#((#((((((((((((((((#######(###########(######(##((*(####.##((((((((/*((((((((,(((#(((((((((((((((((((((((((((((((((((((((((((#(              ,/##(##(((((((((((((((((((((
(((((((((((((((((*/(((((((((((#((#(((((((((((((((((####*%######/####/###/(###/#######(((((##(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#, ..*/####((((((((((((((((((((((((((((((((
(((((((((((((((((,/,//,*(#,(.,/,/ #./,/(/.****(/*/./(.#.(*(((.#,#(.(.(.(*/,*/,#,*/.#,#(*(*(.,*/**(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
(((((((((((((((((,(,.(,/(((./(.,#..,/*((/../,/(.,*,./,*,#..*..#,##*..(.#*(,*#,#///,.*#(/./..,.,(.(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((###(((((((((((((((((((((((((((((
((((((((((((((((((((((((((#((#(#####((((((((((########(######(#####################%##############(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((######(((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((##((#############(##(##############%#####%%###%########(########((#(((((((((((((((((((((((((((((((((((/(/(((((((((((((((((((((((##########((((((((((((((((((((((((((((((
((((((((((((((((((((((((((#(##(#######(#################%#%###########%####((((##((((##############((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((##############(((((((((((((((((((((((((((
(((((((((((((((((.((*(,/,.(,(.,(*#,,/(,/#((/*#,*,,#,,( (/#,/##/,(.,(/,*(,,(/,,#//,,#*,*##*(,,/##./.,,#,,((*.(,,(,,*./(..,,/,,(*,,,,((,*(.(,*(,,(,,(,,*./,.*(*,(*,(#**,/,,#,/**.##(###(((((((((((((((((((
(((((((((((((((((.(((*,/.(*,(*//,#,(,/(*##.,/.(,#.((*(.#%(%.##.##,&,,#.(*(.,*((**(,#.*#%%,#.(*#%,#.#,**###(,*/(((,/.#(*/./*,**,(.(.((,*/.,/##.(//((,(./*,(,/.#%,#(#/,%,*////#,#######(((((((((((((((((((
((((((((((((((((((((((((*(#(###############################################(*/######/*(########################(((######(((((((((((((((((((((####((((((((((((######################(((((((((((((((((((((
/((((((((((((((((((((((((((##############################################(############%##################################################################################%############((((((((((((((((((
/(((((((((((((((((((((((((#################################%%###################################################################(##################################%####################((((((((((((((((
/((((((((((((((((((((((((##############################################################################################################################%%%%%%%%##########################(((((((((((((((
/((((((((((((((((((((((((##########################################%%######################################################################################%%#####%%%##################(((((((((########
/((((((((((((((((((((((((###############################%%%%%####################################################################%%##########%%%%%%%%%%%%%%%%##############################((((#########
/((((((((((((((((((((((((##############################%%%%##%#####%#############################(/*,......................,,.,.,**,,,,,,,,,,,****/((##%%########################%######################
/((((((((((((((((((((((((###############%%########%########%%%%%%%%%%%%##############(/,,,,*//((###%%%%%%%%%##(###%%%%%%%#(//%.,*,/%&&&&&&&&&&&&&&&&%%#(/**,***/(#########%%%%%#########################
///////(((((((((((((((((((###############%%#####%%%%%%%%%%%%%%%%%%%%%%#########%(,,*,,*/((/(#%%%%%%%%%%%%%%%##%&%%%%%%%###&/.,*(&&&%%%%%%%%%%#&&&&%%%%%%%%&%&&%/*/**/%#######%%%########################
///////////((((((((((((((((#######################%%%%%%%%%%%%%%%%%########%(.,,,**/((((##((((##(((//**/%%%%&&%((((((%%&&*.,,%&%%%%%&%/(//(/%%%&&&%/((((((((#(((@&#%##################################((
///////////////(((((((((((((((##################%%%####%%%%%%%%%%%%####%(,,,,**/(((#((#####((((((/######%%%&&%%&#(((&(&(.,,&&%#(##%%#&%&%%#((%%%&%&%(((((((((((##%&&%##((#%#######################(((###
///////////////(((((((((((((############################%%%%%%%%#%##%.*,***/((#((####((((((((((/##,(//,/(#%%&&%&&((&%( ,,%&&%####%%%&&&&&%&((#%#&&&&(/(((((((((/(@%#&&#%#(/%############################
/////////////////(((((((((((((###################%########%%%%%%%/.,,,**/(########(((###((((#(*#(,##/,*(#(#%&&&%%(%#..,/&&&&&%#%%%%%%&&&%&&&%%%%&&&&&%%%%%%%%%(((/&##/&@&%#(#%##########################
*////////////////((((((((((((################%########%%%%#%*  *,,**/((#(((#(((/(((((((####%#,(/,(##%%//((,*/*/*%(..,*&&@&(..    ..*#%%&%&&&%%#%#&&&&%%%%&&&%%#(//****,,,******(###%####################
****//////////////////(((((((((((/(((((((((((((((((((((###(%#*((##%#%%%%#%%##%%%&&&&&&%&%%%%%#%%####%%#(*,****%#..,*&&&&&     .,,*/(######%&&&@&%/*,,**************************#&#(#########%%%%########
**********//////////////////////////////////////(//*,..........                            .....,,,*****,,.. ...,*#&&&@&@&&&&@@@@@@@@&,*,****,***************/////((((((((/////((#@#////////////////////
************/////////////////////////////*........                                                ... ..,,*///*****,//(#%%##(((/***************///////////////////////(#(#%/**/((//(((((((((((//////////
************/////////////////(////*.   .                                                     ...,,,***,,*****,,,,,,,,,******/((((((////////***/*(***/(/////////////////(((((/((((//#,************///////
************///////////////(((.                                                     . ...........,..,,,,,,,,,,,,****///////////(((//////******///(///(/////((((((((((((((((////(((/((///////////////////
***************************/                                                       ./(#/,,,,*/(#&&&*,,,****************/****/**/////////////(/((/(((((((((((((((((((((((((///(((((((#///////////////////
,************************#.,                                          ..,**/*,..*/(##(%%%%&&%&&(.,*,,,*****************///////////(((((((((((((((((((((((((((((((((((((((((((@@@@@#(#///////////////////
,**************/////////%(,.                                   ,//,. .((.,**,.*,  ,**(&&&&&@,,,*,,,,,,***//////**//////(///////((((((((((((((((((((((((((((((((((((((((((((@@@@@@@@@#(////////////(((///
,***************////////((#&&&&&@&@@&@%#%%(*,....       .*.     /%%#/.,. .*,,,,,.*/,/%%@@/,,,,,,,,,*//////////////////((/(((((((((((((((((((((((((((((((((((((((((((((/((&@@@@&&@@@@@#.,,****///////////
,****************//////..           .#%%%##*,*//((##%&&%%%/#(///**,(%&%* ,,. .//,.,/&&%.***,,,,,,////#@@@@@@@@@@#//(//((((((((((((((((((((((((((((((((((((((((((((((((((@@@&&&%#%&@@@#***///////////////
,****************//*//.. .  #@&&@@@@&@%#(/,.                       .((%#(/,.      .,,*,,,,,,,,,(//(@@@@@@@@@@@@@@@%/(/((((((((((((((((((((((((((((((((((//((((###((((((&@@%@@&%&&%@@@#/////(((((((((((((
,,***************/////.#*.. ((%%&&@&&&&@&@&&@&@&@@%@&%@@#&#             .......,,,,,,,,,,,,,,*//(@@@@@@@@@@@@@@@@@@@((((((((((((((((((((((//////((((((((((((((((((((((#@@@&&%&%%&%%@@#((((((((((((((((((
,,,,**************////.##%, (............    ..,#%%&&%&%%%&/. ...................,,,,,,,,,,*///%@@@@@@%&%%%%%%@@@@@@@((((((((((((//////(((((((((((((((((((/(//###%##(#@@@@%&%%%&&%%@(((((((((((((((((((/
,,,,,,**************/**,... (................. ./&%&&%&&%&*.......................,,,,,,,,*///@@@@@&%&&&%&&&#&%%@@@@@%((((((//((((((((((((((((((((###%%%%###(((######(@@@@%%&(%&%#@%((((((((((((((((((((
,,,,,,***********/****,,,/&&&@@@&&%#/*.    .... /&%&&%&&&......................,,,,,******///@@@@@&&%%&%%&%%%&&%&@@@@&((((((((((((((((##%#%%%#(/((######%%%%%%%&&@@@@@@@@@@%#%@&%&@#(((((((((////(((((((
,,,,,,,,,,,,..,..........#.#&@@@&&&@@@&@&@@&&@@&@&%@&&%&..**//((((@@@@@@@@@@&/**,,*******///&@@@@@%&&@%&%%%&%&%%%@@@@&((#########(///(#########%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@&%%###((((/(////////(/
,,,,,,,,**********/////*  &&&#(*,,,..,,**/(#&&@&@@&@@&*.,..,,,,%#/#(((#%(/%#%&&@/*******///(@@@@@&%&&%#&%%%%&&&#%@@@@#(#((#######%%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%%####((((((((((((((
,,,,,,,***********//////*,.   .,(%@@@&&&@@&%#(/,,,,,,,**,,,.#%%///((((#/((#%%&&@@@ */*/////@@@@@@&%%%%%%#&%%&&%#&@@@@(##%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%%%%#%%####((((////////(/
,,,,,,,*************////*,&@@&%%#(/*,...    .,/(#%%&&@&&&&&&&&@&&&&%%%#(/*,.   ..*****/*/((@@@@@@@%%&%%&&#%&&%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%#####((((//////////////
,,,,,,,,**********///////////(%%&@@@@@@@@@@&&%%##((///*,.....,,,.................,,,****/(#@@@@@@@@###&@&%%@%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%#########((((((/////////////***,
,,,,,,,,,**********/////////#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&, .. ...............,,,**//(#&@@@@@@@@@@&%%###%#%@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&%%%%%%%%%%%%%%############(((((((((//////////**......,..,
,,,,,,,,,,*********/////////((#%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%########(((((((////(((//////**,,.............,,,,*
,,,,,,,,,,********///////////((((((#####%%%%%&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%########((((((((//////////////*,......,....,,....,,*///((((//
.,,,,,,,*********/////////////////((((((((((((#########%%%%%&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@&&&&%%%%%%%%%%%%%%%%%###########((((((((((////////////***,,...........,,,,.....,,**///////////////
.,,,,,,,,*********////////////////////(((////((((((((((((((#############%#%%%%%%%%%%%%%##################################((((((((((//(///((//////////*,,..........,...,,...,****////////////////////////
""")
typingPrint("           ***DISCLAIMER***         \n")
time.sleep(2)
typingPrint("        THIS IS A VERY HARD GAME       \n")
time.sleep(1)
typingPrint("Hello Driver\n\n")
time.sleep(1)
driver_name=typingInput("\n\nWhat is your name?\n\n")
typingPrint(f"\n\nHello {driver_name}!\n\n")
time.sleep(1)
race_number=typingInput("\n\nWhat is your race number?\n\n")
typingPrint(f"\n\nWelcome Racer number {race_number}!\n\n")
start_race()