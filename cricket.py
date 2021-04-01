import random
# Chinese cricket

print("This game is for 6 deliveries")
def cpu():
    rand= random.randint(1,6)
    return rand

sum=0


for x in range(1,7):

    ply = int(input("Play your shot : \n"))
    a= cpu()
    print(a)
    if ply!=a :
        sum =sum + ply
        print("Nice shot, ur score is" ,sum)
    else:
        print("Oops u'r out")
        break

print("Ur total score is:",sum)

# computers turn and ur bowling
print("computers turn: Be ready for bowling")

cpu_score =0
for y in range(1,7):
    if cpu_score <= sum:
        ply = int(input("Bowl to batsman \n"))
        a= cpu()
        print(a)
        if ply!=a and cpu_score<=sum :
            cpu_score = cpu_score + a
            print("Nice shot by batsman:  score is",cpu_score)
        elif ply==a and cpu_score ==sum:
            print("Bowled")
            print("Computer score" +str(cpu_score) + "   ur score  " + str(sum))
            print("match is tied")
            break
        elif ply ==a and cpu_score<sum :
            print("Bowled What a Beauty")
            print("Computer score" +str(cpu_score) + "   ur score  " + str(sum))
            print("Hooray!  U Won")
            break
        else:
            print("End of Over")
            print("Computer score" +str(cpu_score) + "   Your score  " + str(sum))
            print("Hooray!  U Won")
    elif cpu_score>sum:
            print("you Lost")
            break
            