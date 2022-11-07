def romanNumburs(number):
    sum = 0
    for i in range(len(number)):
        if number[i]=="I":
           sum+=1
        elif number[i]=="V":
            if number[i-1]=="I" and i!=0:
                sum+=3
            else:
                sum+=5
        elif number[i]=="X":
            if number[i-1]=="I" and i!=0:
                sum+=8
            else:
                sum+=10
        elif number[i]=="L":
            if number[i-1]=="X" and i!=0:
                sum+=30
            else:
                sum+=50
        elif number[i]=="C":
            if number[i-1]=="X" and i!=0:
                sum+=80
            else:
                sum+=100
        elif number[i]=="D":
            if number[i-1]=="C" and i!=0:
                sum+=300
            else:
                sum+=500
        elif number[i]=="M":
            if number[i-1]=="C" and i!=0:
                sum+=800
            else:
                sum+=1000
    return sum

print(romanNumburs("MMMCDXC"))
