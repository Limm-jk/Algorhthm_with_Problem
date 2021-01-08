bill = [1,2,5,10,20,50]

def rec(bill, money:int):
    if len(bill) == 1:
        if money % bill[0] == 0:
            return 1
        else: 
            return 0
    curr = bill.pop()
    count = 0
    while money > curr:
        count += rec(bill, money)
        money -= curr
        
    return count

print(rec(bill, 100))
    