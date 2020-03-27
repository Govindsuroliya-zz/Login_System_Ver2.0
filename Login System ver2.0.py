# Welcame to Login System Version 2.0 .
with open("serectxpathlogqual.tid") as IDpath:
    log_ID = str(IDpath.readline())
    print(log_ID)
with open("serectxpathlogpassqual.tid") as PASSpath:
    log_PASS = str(PASSpath.readline())
    print(log_PASS)
# we are create login system in python by simple Logic.
print("Welcame to Login System Version 2.0\n")
print("© Copyright 2020 Ti Corporation.\n")
# we put User Inputs in Varibles.
print("If you want to exit this program plase press Q\n")

ID_system = input("Please Enter Your ID.\n")
print("\n")
while ID_system != log_ID:
    if ID_system == "q":
        break
    print("Acess Not Allowed\n")
    ID_system = input("Please Enter Your ID.\n")
    print("\n")
# here serect work in script
if (log_ID == ID_system):
    PASS_system = input("Please Enter Your PASSWORD.\n")
    print("\n")
    while PASS_system != log_PASS:
        print("Acess Not Allowed\n")
        PASS_system = input("Please Enter Your PASSWORD.\n")
        print("\n")
    if (log_PASS == PASS_system):
        print("Acess Allowed\n")
        print("*******************************************\n")
        print("If you want to change the ID and Password. Please press C \n")
        print("*******************************************\n")
        change = input()
        if change == "c":
            value = input("Enter New ID = \n")
            with open("serectxpathlogqual.tid", "w") as op:
                op.write(value)
            print("Your ID is changed Successfully !")
            value = input("Enter New Password = \n")
            with open("serectxpathlogpassqual.tid", "w") as op:
                op.write(value)
            print("Your Password is changed Successfully !")
