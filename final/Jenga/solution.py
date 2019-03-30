def play(single,double):
    if double%2 == 0 and single %2 == 0:
        return "Fatih"
    else:
        return "Onur"

n = int(input())

for i in range(n):
    single_mv = 0
    double_mv = 0
    k = int(input())
    for e in range(k):
        x,y,z = list(input())
        count = [x,y,z].count("-")
        if count == 3:
            double_mv += 1
        elif count == 2 and y != "*":
            single_mv +=1
    print(play(single_mv,double_mv))
