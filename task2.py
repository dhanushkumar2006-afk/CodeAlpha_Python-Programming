print("WELCOME TO SKYLINE")

while True:

    a = input("you: ").lower()

    if a in ["hi","hello","hey"]:
        print(f"bot: {a}, what's today what are you going to do")
    elif a in ["how are you","how do you do"]:
        print(f"bot: I am fine thank you , what about you ")
    
    elif a in ["who are you","what is your name","what about you "]:
        print(f"I am a chat bot, my name is skyline . I will help you when you in some diffucult times")
    elif a in "who created you":
        print (f"I am created by manohar and co-founder harshith")
    elif a in ["bye","good bye","see you later"]:
        print(f"bot: {a}, have a great day")
        break
    else :
        print (f"bot: sorry i can't understand your question")
        
        