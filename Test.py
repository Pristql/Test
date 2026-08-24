print("Guess the secret number 1-50!")
secret=9
g1=int(input("Enter your first guess here: "))
g2=int(input("Enter your second guess here: "))
g3=int(input("Enter your third guess here: "))
g4=int(input("Enter your fourth guess here: "))
g5=int(input("Enter your fifth guess here: "))
if g1==secret:
    print("Correct!")
elif g2==secret:
    print("Correct!")
elif g3==secret:
    print("Correct!")
elif g4==secret:
    print("Correct!")
else print("You ran out of tries")

