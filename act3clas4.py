print("Enter Marks Obtained in 4 Subjects:")

math=int(input("math:"))
english=int(input("english:"))
science=int(input("science:"))
hindi=int(input("hindi:"))

sum = math+english+science+hindi
print("sum of math,english,science,hindi",sum)

perc=(sum/400)*100

print(perc)