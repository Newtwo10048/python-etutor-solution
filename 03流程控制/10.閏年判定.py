#10.閏年判定
n = int(input())
if n % 400==0:
    print("Bissextile Year")
else:
    if n % 4==0:
        if n % 100 ==0:
            print("Common Year")
        else:
            print("Bissextile Year")
    else:
        print("Common Year")
#需要搞清楚哪個先判斷：有400就是潤，有4但有100是平沒100是潤