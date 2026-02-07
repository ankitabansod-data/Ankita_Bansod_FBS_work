# write a program to calculate the percentage of student based on marks of any five subject.

s1=int(input('Enter marks of sub 1:'))
s2=int(input('Enter marks of sub 2:'))
s3=int(input('Enter marks of sub 3:'))
s4=int(input('Enter marks of sub 4:'))
s5=int(input('Enter marks of sub 5:'))
total=s1+s2+s3+s4+s5
#Total marks of each sub is 100
Percentage=(total/500)*100
print("Total marks:",total)
print("Percentage:",Percentage)

