import random 
print("WELCOME TO HANGMAN GAME")
l = ["mango","apple","banana","orange","strawbarry"]
a = random.choice(l)
display = ["-"]*len(a)
attempts = 0 
while attempts <6:
    b = input("GUSS A LETTER :")
    found =False
    
    for i in range (len(a)):
        if a[i] == b :
            display[i] = b
            found= True

    print(" ".join(display))
    
    if not found:
        attempts+=1
        print (f"WRONG YOU HAD ONLY {6 -attempts}:")

    if "".join(display) == a:
        print("Your are the winner🎉")
        break

if "".join(display)!=a:
    print(f"you lost! The word {a}")