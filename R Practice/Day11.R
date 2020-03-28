# Day 11:
# Question 1:
R<-read.csv(file.choose(),head=TRUE)
R

total = rowSums(R)
R1<-cbind(R, total)
R1

# Question 2:
# 1:
list1 <- list(observationA = c(1:5, 7:3),observationB=matrix(1:6,nrow=2))
list1

# (a):
?lapply
a<-lapply(list1,length)
a

# (b):
b<-lapply(list1,sum)
b

# (c):
a<-lapply(list1,class(list1$observationA))
a

b<-lapply(list1,class(list1$observationB))
b


