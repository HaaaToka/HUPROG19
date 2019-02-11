def play(single,double):
    if double == 1:
        return "A"
    elif (double%2) ^ (single%2) == 1:
        return "A"
    else:
        return "B"
fl = open(input(),"r")
n = int(fl.readline())
#n = int(input())
single_mv = 0
double_mv = 0
for i in range(n):
    x,y,z = list(fl.readline())[:3]
    #x,y,z = list(input())
    count = [x,y,z].count("-")
    if count == 3:
        double_mv += 1
    elif count == 2 and y != " ":
        single_mv +=1
print(play(single_mv,double_mv))


    
