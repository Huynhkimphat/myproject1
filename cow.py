import random
def test(x, y):
    cowbull = [0,0] 
    for i in range(len(x)):
        if x[i] == y[i]:
            cowbull[0]+=1
        elif x[i] in y:
            cowbull[1]+=1
    return cowbull
x = str(random.randint(1000,9999)) 
print(x)
guesses = 0
while True:
    
    y = input("Guess")
    if y == "exit":
        break
    cowbullcount = test(x,y)
    guesses+=1
    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
    if cowbullcount[0]==4:
        print("You win the game after " + str(guesses) + "! The number was "+str(x))
        break 
    else:
        print("Your guess isn't quite right, try again.")