#eletricitybillprediction

id=int (input("enter the user id:"))
name=input("enter the name:")
unit=int(input("enter the unit"))
if unit>=300:
    amount=100+400+(unit-300)*3
elif unit<=100:
    amount=100+(unit-100)*2
else:
    print()
    
if amount<=50:
    bill=50
elif amount>=1500 or amount<=1500:
    bill=amount+amount*0.15
else:
    print("no data")
    
    
    
print("user id:",id)
print("user name:",name)
print("unit consumed:",unit)
print("bills:",bill)
#codebymugundhan
