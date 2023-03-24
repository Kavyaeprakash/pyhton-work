# i=0
# while i<=10:
#     print(i)
#     i+=1

password = "cybersquare"
guess = ""
while password!=guess:
    guess =input('Enter the password: ')
    if password==guess:
        print("Login success:")
    else:
        print("Incorrect password...try again.")
        