# Question 1:
# (a)-(d)
student <- list("Name"="Srinivas","RollNo"=37,"Gender"="M","Marks"=c(44,45,65,66,48))
student

# (a) Average of Marks
student[[4]]
avg_marks=mean(student[[4]])
avg_marks

# (b) Store the Roll No and Marks to another list.
student1<-list("RollNo"=student[[2]],"Marks"=student[[4]])
student1

# (c) Modify the mark for the 5 th subject as 100
student1[[2]][5] = 100
student1

# (d) Prepare a new vector with the names of the 5 subjects
subjects<-list(subject1="Math",subject2="Physics",subject3="Chemistry",subject4="Social",subject5="Telugu")
subjects

# (e) Attach it as the last item in the list
l3<-append(student,subjects)
l3

# Question 2:
# (a) Calculate B= 2A
A<-matrix(1:4,2)
A
B=2*A
B

# Question 3:
# (a) Check that A 3 = 0 where 0 is a 3 × 3 matrix with every entry equal to 0.
A=matrix(data=c(1,1,3,5,2,6,-2,-1,-3),nrow=3,ncol=3,byrow = TRUE)
A
B = A*A*A
B

# Question 4:
B<-matrix(data=c(rep(c(10,-10,10),times=15)),nrow=15,byrow = TRUE)
B
D<-t(B)
D
C<- D%*%B
C

# Question 5:
# (a)
m1<-matrix(1:15,nrow=3,ncol=5)
m1
# (b)
colnames(m1)<-c("p1","p2","p3","p4","p5")
rownames(m1)<-c("Alice", "Bill","Sara")
m1
# (c) Calculate the mean for all columns
m2<-c(m1)
m2
m3<-mean(m2)
m3

# Question 6:
category<-factor(c("Demographics","Convenience","Quality","Performance","Quality","Performance","Demographics"))
category




