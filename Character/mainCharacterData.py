MainCharacter = {
    "Name" : 'defaultName',

    "Max health" : 100,
    "Health" : 100,
    "Stamina": 100,
    "Max stamina": 100,
    "Stamina regen": 10,
    
    "ATKbuff" : 0,
    "DEF": 1,
    "Shield": 3,

    "Level": 1,
    "Exp cap": 30,
    "Exp": 0,

    "Gold" : 50,        
    "Items" : [
        {
            "Name": "Bread1",
            "Type" : "Food",
            "Health regen" :15,
            "Stamina regen" : 5,

        },
        {
            "Name": "Bread2",
            "Type" : "Food",
            "Health regen" : 15,
            "Stamina regen" : 5,

        },
        {
            "Name": "Candy",
            "Type" : "Food",
            "Health regen" : 10,
            "Stamina regen" : 0,

        },
        {
            "Name": "Bottle of Water",
            "Type" : "Food",
            "Health regen" : 0,
            "Stamina regen" : 25,

        },
        {
            "Name": "Bandage",
            "Type" : "Food",
            "Health regen" : 25,
            "Stamina regen" : 5,

        },
        
    ],

    #NOTE: Weapon Damage
    "Weapon" : "Bare Hand",
    "Damage" : 4, 

    #NOTE: Skill
    "Skills" :  [
        ###NOTE: skill tấn công
        {
        "id" : 1,
        "Name": "Tackle",
        "Minimum level": 1, 
        "Stamina cost": 7,

        "Damage": 5,
        "Healing": 0, 
        "Shield": 0,

        "Cooldown" : 0,
        "On cooldown": 0,
        },

        {
        "id" : 2,
        "Name": "Quick Attack",
        "Minimum level": 2,
        "Stamina cost": 15,

        "Damage": 8,
        "Healing": 0,
        "Shield": 0,

        "cooldown": 1,
        "On cooldown": 0,
        },

        {
        "id" : 3,
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Stamina cost": 24,

        "Damage": 14,
        "Healing": 0,
        "Shield": 0,

        "cooldown": 3,
        "On cooldown": 0,
        },

        ###NOTE: skill hỗ trợ 
        {
        "id" : 4,
        "Name": "Gentle Mist",
        "Minimum level": 2,
        "Stamina cost": 22,

        "Damage":0,
        "Healing": 12, 
        "Shield": 0,

        "Cooldown" : 4,
        "On cooldown": 0,
        },
    ]   
}

