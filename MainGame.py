import time
import random

### Folder: Data
from Character import mainCharacterData
from Character import MonsterData 



### Folder: TextStoryData
from TextStoryData import Credit
from TextStoryData import Opening
from TextStoryData import Menu
from TextStoryData import Chapter1

### Folder: FightFC 
from FightFC import fightingFC

### Folder: WIPtextData
from WIPtextData import WIPtext




###########NOTE Các function chạy game
def menuFC(x):
    if (x == "C" or x == "c"):
        ## Show Credit 
        Credit.creditShow()
        Menu.Menu()
    else:
        ## Nếu điền sai
        print("Wrong Command!!")
    
def skipStory(x):
    while (x != "y" and x != "Y" and x != "n" and x != "N"):
        print("Wrong Command!!")
        x = str(input("Do you want hear a story? (Y/N): "))

    if (x == "Y" or x == "y"):
            #Loading
        Opening.loading()
        #Cốt truyện
        Opening.Opening()
        #Cốt truyện thằng main 
        Opening.heroOpening()
        # đặt tên cho nhân vật
        heroName = str(input("His name is: "))
        mainCharacterData.MainCharacter["Name"] = heroName
    if (x == "N" or x == "n"):
        print("seriusly bro????")
        time.sleep(1)
        heroName = str(input("Hero's name is: "))
        mainCharacterData.MainCharacter["Name"] = heroName

##################TODO Lắp ráp game

##NOTE: Menu game 
#Khởi tạo Menu
Menu.Menu()


#chọn Credit hoặc Start
startOrCredit = str(input("S/C ? "))

while (startOrCredit != "S" and startOrCredit != "s"):
    menuFC(startOrCredit)
    startOrCredit = str(input("S/C ? "))



##NOTE: Start game
if(startOrCredit == "S" or startOrCredit == "s"):
    skipStoryQuestion = str(input("Do you want hear a story? (Y/N): "))
    skipStory(skipStoryQuestion)
    ##bắt đầu vào chapter 1
    Chapter1.Chapter1_1()
    # đánh nhau với cướp
    fightingFC.fight(mainCharacterData.MainCharacter,MonsterData.TheRobber)

    #Work in process
    WIPtext.WIPtext()



