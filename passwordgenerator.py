import random 
#https://howsecureismypassword.net/
def start():
  x = 0
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
  y = 0
  length = int(input("How many characters?\n"))
  name = "exit"
  while x == 0:
    password =  ''
    for c in range(length):
        password += random.choice(chars)
    print("PASSWORD:" + password)
    letter = input ("PRESS ENTER FOR NEW PASSWORD OR TYPE exit TO EXIT or TYPE length TO CHANGE LENGTH:\n")
    if letter == "ENTER":
        print ("\n")
    elif letter == "exit":
        x = 1
    elif letter == "length":
        length = input ("How many characters?\n")
        length = int(length)
start()
