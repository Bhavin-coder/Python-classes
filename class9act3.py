num=int(input("enter a number:"))
sum=0
temp=num
while temp>num:
    digit=temp%10
    sum +=digit**3
    temp//=10

if num==sum:
    print(num ,"is an amstrong number")
else:
    print(num,"is not an amstrong number")