# R Exam
# Question 1:
A<-matrix(c(1,1,3,5,2,6,-2,-1,-3),nrow = 3,ncol = 3,byrow = TRUE)
A

B<-A%*%A%*%A
B

# Question 2:
?list

student<-list("Name"="Srinivas","Roll No"=44,"Gender"="M","Marks"=c(22,33,44,55,66))
student

# a
mean(student[[4]])

# b
student1<-list(c(student[[2]]),student[[4]])
student1

# c
student[[4]][5]=100
student
