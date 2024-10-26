def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip() # stripping out the carriage return from our line
            user, passw = data.split("|") # Splitting each line on "|"
            print ("User:", user, "- Password:", passw)

def add():
    name = input ("Account Name: ")
    pwd = input ("Password: ")
    
    with open ("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input ("Add or View a password? Type q to exit! ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print ("Invalid mode")
        continue