
"""

1 <= Q <= 10
1< N <= 10^7

"""

q=int(input().strip())
# if not 1 <= q <= 10:
#     print("1Constraints")

for _ in range(q):
    n=int(input().strip())
    # if not 1 < n <= 10**7:
    #     print("2Constraints")

    txt=[]
    tam,yarim=0,0
    """
    yarim -> *-- , --*
    tam -> -*-
    """
    for __ in range(n):
        txt.append(input().strip())

        # for chr in txt[-1]:
        #     if not (chr=="*" or chr=="-"):
        #         print("3Constraints")

        if txt[-1][1]=="*":
            continue
        else:
            if txt[-1][0]=="-" and txt[-1][2]=="-": # ---
                tam += 1

            elif txt[-1][0]=="-" and txt[-1][2]=="*": # --*
                yarim += 1

            elif txt[-1][0] == "*" and txt[-1][2] == "-":# *--
                yarim += 1

    if  yarim%2==0 and tam%2==0:
        print("Fatih")
    else:
        print("Onur")


"""

ONUR basliyor ve ilk hamlesinden sonra yarim kalan sayisini cift yapabiliyorsa sonraki hamlelerde Fatih ne yaparsa aynisini yaptigi durumda ONUR kazanir

2
3
---
--*
---
3
---
-*-
---

"""