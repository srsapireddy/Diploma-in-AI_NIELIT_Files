# Question 1:
student<-data.frame(Age=c(25,31,23),Height=c(177,163,190),Weight=c(57,69,83),Sex=c("F","F","M"))
student
rownames(student)<-(c("Alex","Lilly","Mark"))
student

# Question 2:
student1<-data.frame(Work=c("No","No","Yes"))
student2<-cbind(student,student1)
student2

# (a):
class(student2$Age)
class(student2$Height)
class(student2$Weight)
class(student2$Sex)
class(student2$Work)

# (b):
mean(student2$Height)

# (c):
bmi<-student2$Weight/((student$Height)/100)^2
bmi

# (d):
# bmi > 25 -> False, else True
health<-(bmi>25)
health
student2
student3<-cbind(student2,health)
student3

# Question 3:
r1 <- read.table(file.choose()) 
r1
# Question 4:
r2 <- read.csv(file.choose())
r2

# Question 5:
A<-array(1:20,c(2,3,3),dimnames = list(letters[1:2],LETTERS[1:3],c("M1","M2","M3")))
A

# Question 6:
# (a):
mtcars
head(mtcars)
m<-data.frame(mtcars$mpg,mtcars$cyl,mtcars$hp)
m
head(m)

# (b):
length(mtcars)
df<-data.frame(rbind(head(mtcars,5),tail(mtcars,5)))
df

# 7.
# (a):
add <- function(a=1,b=1)
{
  return (a+b)
}

add()

# (b):
add <- function(a=4,b=7)
{
  return (a+b)
}

add(b=7,a=4)

# 8:
# (a):
ls()

# (b):
getwd()

# (c):
# setwd(/home/ai37)

# (d):
list.files
