startyear=int(input("enter the start year:"))
endyear=int(input("enter the end year:"))
print("the leapyear between",startyear,"and",endyear,"are:")
for i in range(startyear,endyear):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)