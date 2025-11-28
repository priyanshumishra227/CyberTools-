"""An authentication simulator is just a tiny imitation of how real systems decide whether someone is allowed in. Think of it as a low-stakes rehearsal for the big cybersecurity world: a user types something in, the program checks it, and either welcomes them or slams the imaginary door."""


username = input("Enter the username: ")
password = input("Enter the password: ")

if username == "admin" and password == "python123":
    print("Access Granted")

else : 
    print("Either username or password is wrong")