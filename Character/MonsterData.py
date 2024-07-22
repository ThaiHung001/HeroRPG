TheRobber = {
    "Name" : "The Robber",
    "Health" : 100,
    "Max health" : 100,
    "Level" : 2,
    "ExpDrop" : 42,    

    "ATK" : 0,
    "DEF" : 0,

    "Live": True,

    "ACT" : [
        {   
            "Name"  : "TALK",
            "Dialog" : "You try to talk with him, but he didnt listen.",
            "ATKbuff" : 0,
            "DEFbuff" : 0,
        },
        {
            "Name"  : "INSULTS",
            "Dialog" : "You insults him, the corner of his eyes flashed with anger.",
            "ATKbuff" : +3,
            "DEFbuff" : -2,
        },
        {
            "Name"  : "REMIND ABOUT FAMILY",
            "Dialog" : "You see the ring on his finger, you remind him of his family, he seemed momentarily distracted.",
            "ATKbuff" : 0,
            "DEFbuff" : -1,
        },
    ],

    "Information" : "The Robber, He was a silent figure, eyes bright as lanterns, and hands as quick as cutting the wind.\nA black cloak covered his face, a knife shining under the magical moonlight in his hand",
    "Weapon": "Knife",
    "Skills" : [
        {
            "id" : 1,
            "Name": "Quick punch",
            "Damage": 3,
                
        },
        {
            "id" : 2,
            "Name": "Strong kick",
            "Damage" : 4,
        },
        {
            "id" : 3,
            "Name" : "slice",
            "Damage" : 7
        },

    ],
    "Mercy dialog" : [
        'You want to mercy for the robber, but all he wants is your gold',
        'he stabbed you, the last thing you heard is: ',
        '"So stupid!"',
    ],
    "Player dead dialog" : [
        '"It\'s best that you give me the money from the beginning."'
    ],
    "Enemy dead dialog" : [
        'The robber fell down, the robber muttered with a weak voice:',
        '"Looks like today is my unlucky day."',
        'After those words, the robber fainted and lay there.'
    ]
}
