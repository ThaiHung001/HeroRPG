import time 
import random

def fight(player, enemy):
    while player["Health"] > 0 and enemy["Health"] > 0:
        time.sleep(1.5)
        print()
        print('////////////////////////////////////')
        #UI 
        print("Your choice:")
        print("[ FIGHT ]")
        print("[ ACT   ]")
        print("[ ITEM  ]")
        print("[ MERCY ]")
        choice = str(input("What is your next action? (F/A/I/M): "))

        while (choice != "F" and choice != "A" and choice != "I" and choice != "M"):
            print("Wrong Command!!")
            choice = str(input("What is your next action? (F/A/I/M) "))

        ## FIGHT
        if (choice == "F"):
            print("[1. Normal Attack","("+player["Weapon"]+")" ,"]")
            for i in range(len(player["Skills"])):
                print(f"[{i+2}.",player["Skills"][i]["Name"],"(lv."+str(player["Skills"][i]["Minimum level"])+")","(Stamina consume:",str(player["Skills"][i]["Stamina cost"]),") ]")
            print()
            print("[ BACK ]")

            def getUserFIGHTchoice():
                while True:
                    c = len(player["Skills"])
                    fightChoice = input(f"What is your next action? (1 - {c+1},BACK): ")

                    if fightChoice.isdigit():
                        fightChoice = int(fightChoice)
                        if ( fightChoice == 1):
                            return fightChoice
                        elif (2 <= fightChoice <= c + 1 ):
                            if (player["Level"] >= player["Skills"][fightChoice - 2]["Minimum level"]):
                                return fightChoice
                            elif (player["Level"] < player["Skills"][fightChoice - 2]["Minimum level"]):
                                print("You need","lv."+ str(player["Skills"][fightChoice - 2]["Minimum level"]),"to use this skill.")
                            elif ( player["Skills"][fightChoice - 2]["Stamina cost"] < player["Stamina"]):
                                print("You need",str(player["Skills"][fightChoice - 2]["Stamina cost"]),"stamina to use this skill.")
                                
                        else:
                            print("Wrong Command!!")
                    elif (fightChoice.upper() == "BACK"):
                        return "BACK"
                    else:
                        print("Wrong Command!!")
            User_fightChoice = getUserFIGHTchoice()

            if (User_fightChoice == 1):
                print("You chose FIGHT.")
                print()
                print("You use",player["Weapon"],"to attack",enemy["Name"])
                print()
                print("You deal", player["Damage"],"Damage")

                enemy["Health"] = enemy["Health"] -  player["Damage"]
                print(enemy["Name"],"has",enemy["Health"],"health left.")

                if (enemy["Health"] <= 0):
                    enemy["Health"] = 0
                    enemy["Live"] = False

            if ( str(User_fightChoice).isdigit() and  1 < User_fightChoice <= len(player["Skills"]) + 1):
                print("You chose FIGHT.")
                print()
                print("You consume",str(player["Skills"][User_fightChoice - 2]["Stamina cost"]),"stamina to use",player["Skills"][User_fightChoice - 2]["Name"])
                print()

                if (player["Skills"][User_fightChoice - 2]["Damage"] > 0):
                    print("You deal", player["Skills"][User_fightChoice - 2]["Damage"],"Damage to",enemy["Name"])
                    enemy["Health"] = enemy["Health"] -  player["Skills"][User_fightChoice - 2]["Damage"]
                    if (enemy["Health"] <= 0):
                        enemy["Health"] = 0
                        enemy["Live"] = False
                    print(enemy["Name"],"has",enemy["Health"],"health left.")

                if (player["Skills"][User_fightChoice - 2]["Healing"] > 0):
                    print("You heal",player["Skills"][User_fightChoice - 2]["Healing"],"health.")

                    player["Health"] = player["Health"] + player["Skills"][User_fightChoice - 2]["Healing"]
                    print("You now have",player["Health"],"health")

                player["Stamina"] = player["Stamina"] - player["Skills"][User_fightChoice - 2]["Stamina cost"]
                if (player["Stamina"] <= 0):
                    player["Stamina"] == 0
                print()
                print("You now have",player["Stamina"],"stamina left")
                

            if (User_fightChoice == "BACK"):
                continue

        ## ACT 
        if (choice == "A"):
            #ACT UI
            print("[1. PLAYER DETAIL ]")
            print("[2. ENEMY DETAIL ]")
            print("[3. PROBE ]")
            if ( len(enemy["ACT"]) > 0):
                for i in range(len(enemy["ACT"])):
                    print(f"[{i+4}.",enemy["ACT"][i]["Name"],"]")
            print() #nothing
            print("[ BACK ]")

            ####Các lựa chọn
            #enemy private ACT choice
            def getUserACTchoice():
                while True:
                    if (len(enemy["ACT"]) == 1):
                        actChoice = input("What is your next action? (1-4, BACK): ")
                    else:
                        b = str(len(enemy["ACT"])+3)
                        actChoice = input(f"What is your next action? (1 - {b}, BACK): ")

                    if actChoice.isdigit():
                        actChoice = int(actChoice)
                        if 4 <= actChoice <= len(enemy["ACT"]) + 3:
                            print("You chose ACT")
                            print()
                            time.sleep(1)

                            actChoice = int(actChoice)
                            print(enemy["ACT"][actChoice - 4]["Dialog"])
                            print()

                            if (enemy["ACT"][actChoice - 4]["ATKbuff"] > 0):
                                print(enemy["Name"],"+"+str(enemy["ACT"][actChoice - 4]["ATKbuff"]),"ATK")
                            elif (enemy["ACT"][actChoice - 4]["ATKbuff"] < 0):
                                print(enemy["Name"],enemy["ACT"][actChoice - 4]["ATKbuff"],"ATK")
                            enemy["ATK"] = enemy["ATK"] + enemy["ACT"][actChoice - 4]["ATKbuff"]

                            if (enemy["ACT"][actChoice - 4]["DEFbuff"] > 0):
                                print(enemy["Name"],"+"+str(enemy["ACT"][actChoice - 4]["DEFbuff"]),"DEF")
                            elif (enemy["ACT"][actChoice - 4]["DEFbuff"] < 0):
                                print(enemy["Name"],enemy["ACT"][actChoice - 4]["DEFbuff"],"DEF")
                            enemy["DEF"] = enemy["DEF"] + enemy["ACT"][actChoice - 4]["DEFbuff"]
                            
                            break
                        elif 1 <= actChoice <= 3:
                            return actChoice
                        else:
                            print("Wrong Command!!.")
                    elif actChoice.upper() == "BACK":
                        return "BACK"
                    else:
                        print("Wrong Command!!.")
            ACTchoice = getUserACTchoice()
            
            ##lựa chọn thứ 1
            if (ACTchoice == 1):
                print("You chose ACT")
                print()
                time.sleep(1)

                print(player["Name"]+"'s","details: ")  
                print("Health:",str(player["Health"])+"(+"+str(player["Shield"])+")"+ "/"+ str(player["Max health"]))
                print("Stamina:", str(player["Stamina"])+"/"+str(player["Max stamina"]))
                print("Stamina regen per turn:",str(player["Stamina regen"]) )
                print("Level:", str(player["Level"]),"("+str(player["Exp"])+"/"+str(player["Exp cap"])+")" )
                print("DEF:",player["DEF"])
                print("Weapon:",player["Weapon"],"(+"+str(player["ATKbuff"])+")")
                print("Gold:",player["Gold"])

                continue
            ##lựa chọn thứ 2
            if (ACTchoice == 2):
                print("You chose ACT")
                print()
                time.sleep(1)

                print("You have probed",enemy["Name"],"and you got: ")
                print("Health: ",enemy["Health"])
                print("Level: ",enemy["Level"])
                print("Weapon: ",enemy["Weapon"])

                if(enemy["ATK"] == 0):
                    print("ATK buff: 0")
                elif(enemy["ATK"] > 0):
                    print("ATK buff: " + "+" +str(enemy["ATK"]))
                elif(enemy["ATK"] < 0):
                    print("ATK buff: " +str(enemy["ATK"]))

                if(enemy["DEF"] == 0):
                    print("DEF buff: 0")
                elif(enemy["DEF"] > 0):
                    print("DEF buff:" + "+" +str(enemy["DEF"]))
                elif(enemy["DEF"] < 0):
                    print("DEF buff: " +str(enemy["DEF"]))

            ##lựa chọn thứ 3
            if (ACTchoice == 3):
                print("You chose ACT")
                print()
                time.sleep(1)

                print(enemy["Information"])

            # Quay trở lại
            if (ACTchoice == "BACK"):
                continue

        ## ITEM 
        if (choice == "I"):
            a = 1
            for item in player["Items"]:
                print(f"["+ str(a) + ". "+ item["Name"]  +" ]")
                a = a + 1
            if (len(player["Items"]) == 0):
                print("[ You dont have any items ]")
            print()
            print("[ BACK ]")
            def get_user_choice():
                while True:
                    if (len(player["Items"]) == 0):
                        itemChoice = input(f"What is your next action? (BACK): ")
                    elif (len(player["Items"]) == 1):
                        itemChoice = input(f"What is your next action? (1, BACK): ")
                    else:
                        itemChoice = input(f"What is your next action? (1-{a-1}, BACK): ")

                    if itemChoice.isdigit():
                        itemChoice = int(itemChoice)
                        if 1 <= itemChoice <= len(player["Items"]):
                            return itemChoice
                        else:
                            print("Wrong Command!!.")
                    elif itemChoice.upper() == "BACK":
                        return None
                    else:
                        print("Wrong Command!!.")

            user_choice = get_user_choice()
            if user_choice is not None:
                chosen_item = player["Items"][user_choice - 1]["Name"]
                print(f"You use: {chosen_item}")
                print()

                player["Health"] = player["Health"] + player["Items"][user_choice - 1]["Health regen"]
                if (player["Health"] > player["Max health"]):
                    player["Health"] = player["Max health"]
                print("You regen",player["Items"][user_choice - 1]["Health regen"],"heath")

                player["Stamina"] = player["Stamina"] + player["Items"][user_choice - 1]["Stamina regen"]
                if (player["Stamina"] > player["Max stamina"]):
                    player["Stamina"] = player["Max stamina"]
                print("You regen",player["Items"][user_choice - 1]["Stamina regen"],"stamina")

                player["Items"].pop(user_choice - 1)
                continue
            else:
                continue   

        ## MERCY
        if (choice == "M"):
            print("You chose MERCY.")
            time.sleep(1.5)
            for dialog in enemy["Mercy dialog"]:
                print(dialog)
                time.sleep(1)
            print(player["Name"],'is dead. Better next time.')
            break


    #Hết lượt, đến đối thủ đánh
        if(enemy["Live"] == True):
            print()
            time.sleep(1.5)
            ##enemy tấn công
            enemySkill = random.randint(0,len(enemy["Skills"])-1)
            print(enemy["Name"],"has attacked you by", enemy["Skills"][enemySkill]["Name"])
            if(enemy["ATK"] == 0):
                print(enemy["Name"],"deal",str(enemy["Skills"][enemySkill]["Damage"]),"damage")
            elif(enemy["ATK"] > 0):
                print(enemy["Name"],"deal",str(enemy["Skills"][enemySkill]["Damage"])+"("+"+"+str(enemy["ATK"])+")","damage")
            elif(enemy["ATK"] < 0):
                print(enemy["Name"],"deal",str(enemy["Skills"][enemySkill]["Damage"])+"("+str(enemy["ATK"])+")","damage")

            ## Trừ máu của mình
            enemyDamage = enemy["Skills"][enemySkill]["Damage"] + enemy["ATK"]
            if(enemyDamage < 0):
                enemyDamage = 0
            playerShield = player["Shield"]
            player["Shield"] = player["Shield"] - enemyDamage
            enemyDamage = enemyDamage - playerShield - player["DEF"]
            if(enemyDamage < 0):
                enemyDamage = 0
            player["Health"] = player["Health"]  - enemyDamage

            if( player["Health"] < 0 ):
                player["Health"] = 0
            if( player["Shield"] < 0 ):
                player["Shield"] = 0

            print(player["Name"], "have",player["Health"] ,"Health and",player["Shield"],"Shield left")

            
            player["Stamina"] = player["Stamina"] + 10
            if (player["Stamina"] > player["Max stamina"]):
                player["Stamina"] = player["Max stamina"]
            
            if (player["Health"] == 0):
                print()
                print("Your eyes blurred, everything went dark, the last thing you heard before falling was: ")
                for dialog in enemy["Player dead dialog"]:
                    print(dialog)
                    time.sleep(1)
                print(player["Name"],'is dead.')
                break
        else:
            print()
            print(player["Name"],'won this fight.')
            print()
            for dialog in enemy["Enemy dead dialog"]:
                print(dialog)
                time.sleep(1)
            print()
            print("You got",enemy["ExpDrop"],"EXP from",enemy["Name"])
            player["Exp"] = player["Exp"] + enemy["ExpDrop"]

            #### NOTE: CƠ chế tăng level (Sẽ chuyển qua function sau này)
            if (player["Exp"] > player["Exp cap"]):
                player["Level"] = player["Level"] + 1
                player["Exp"] = player["Exp"] - player["Exp cap"]
                player["Exp cap"] = player["Exp cap"] + 14
                print("you have leveled up, you are now","lv." + str(player["Level"]),"("+str(player["Exp"])+"/"+str(player["Exp cap"])+")" )

            break

def levelUpFC():
    print("WIP")