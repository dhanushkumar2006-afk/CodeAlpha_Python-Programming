import re 

with open ("file.txt","r") as wr:
    a = wr.read()

    codes = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", a)

    if codes:
        with open("emails.txt","w") as ml:
            for i in codes:
                ml.write(i+"\n")
            print("email has came")
    else:
        print("no their is no mails")