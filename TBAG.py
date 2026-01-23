"""
Text-Based-Adenture Game!
>Created by Autum Darrell

Created January 23, 2026

Thank you for checking out my little project :D
"""
# Tutorial
print("Hello! Thank you for playing my game. I'm Autum, the creator of this project, and I hope you have fun.\n\nBefore entering this wonderful world, you need a vessel to do your bidding! Let's do that now! I'll ask you some questions and provide you with a method to asnwer. This can be writing text, for example your name, a yes or no prompt, or a list of choices.\nHere are some examples:\n\n\"What is your name?\"\nYou: Your Name\n\n\"Shake hands?\"\n- Y\n- N\nYour Name: Y\nDo note that Y and N are case sensitive.\n\n\"You arrive in town. What will you do?\"\n1. Kill everything in sight.\n2. Make friends\n3. Dance like a lunatic until dawn\n4. Rest and regearn\n5. Nothing... just stand here...\"\nYour Name: 3\n\n")
start = input("All right. That's about all there is to it! Are you ready to start by making your character?\n- Y\n- N\n")
if start == "Y":
  print("Great! Here we go!\n")
elif start == "N":
  print("Ha! I like how you think pal.\n")
else:
  print("Sorry, I didn't get that. Remember, these answerse are case sensitive and need to be capitalized.\n I don't know how to make the game go back a step yet, so sadly, this is the end of the game for you. The program will now exit. Please reopen it to try again.\n\nENDING UNLOCKED: FAIL THE TUTORIAL")
  exit
# Player name
print("One last thing before we begin, what will your name be in this world?")
MCname = input("Enter your name: ")
print("Thanks ", MCname, "! Now it's time to create your character!")
# Character creator
print("Select a race.\n1. Human\n 2. Elf\n3. Orc\n4. Dwarf\n5. Gnome")
MCrace = input(MCname + ": ")
MCrace = int(MCrace)
# Change this to classes later on
if MCrace == 1:
  MCrace = "Human"
elif MCrace == 2:
  MCrace = "Elf"
elif MCrace == 3:
  MCrace = "Orc"
elif MCrace == 4:
  MCrace = "Dwarf"
elif MCrace == 5:
  MCrace = "Gnome"
else:
  print("Sorry. I can't understand you.\nNo fail condition available at this time")
