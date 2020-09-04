# Author: Haorong Xu hxx5086@psu.

gradep1=0
g1=input("Enter your course 1 letter grade: ")
c1=input("Enter your course 1 credit: ")

if(g1=="A"):
  gradep1=4.0
elif(g1=="A-"):
  gradep1=3.67
elif(g1=="B+"):
  gradep1=3.33
elif(g1=="B"):
  gradep1=3.0
elif(g1=="B-"):
  gradep1=2.67
elif(g1=="C+"):
  gradep1=2.33
elif(g1=="C"):
  gradep1=2.0
elif(g1=="D"):
  gradep1=1.0
else:
  gradep1=0.0

print(f"Grade point for course 1 is: {gradep1}")

#----------------------------------------- end of gradepoint1/course1

gradep2=0
g2=input("Enter your course 2 letter grade: ")
c2=input("Enter your course 2 credit: ")
if(g2=="A"):
  gradep2=4.0
elif(g2=="A-"):
  gradep2=3.67
elif(g2=="B+"):
  gradep2=3.33
elif(g2=="B"):
  gradep2=3.0
elif(g2=="B-"):
  gradep2=2.67
elif(g2=="C+"):
  gradep2=2.33
elif(g2=="C"):
  gradep2=2.0
elif(g2=="D"):
  gradep2=1.0
else: 
  gradep2=0.0
print(f"Grade point for course 2 is: {gradep2}")

#----------------------------------------- end of gradepoint2/course2 

gradep3=0
g3=input("Enter your course 3 letter grade: ")
c3=input("Enter your course 3 credit: ")
if(g3=="A"):
  gradep3=4.0
elif(g3=="A-"):
  gradep3=3.67
elif(g3=="B+"):
  gradep3=3.33
elif(g3=="B"):
  gradep3=3.0
elif(g3=="B-"):
  gradep3=2.67
elif(g3=="C+"):
  gradep3=2.33
elif(g3=="C"):
  gradep3=2.0
elif(g3=="D"):
  gradep3=1.0
else:
  gradep3=0.0
print(f"Grade point for course 3 is: {gradep3}")

#----------------------------------------- end of gradepoint3/course3



#final calculation
final=((gradep1*float(c1))+(gradep2*float(c2))+(gradep3*float(c3)))/(float(c1)+float(c2)+float(c3))

print(f"Your GPA is: {final}")