# Day 8
# Question 1:
# (a):
x<-sample(1:6,3000,replace=TRUE)
x

# (b):
x<-sample(30:70,27,replace = TRUE)
x

# (c):
x<-sample(c("H","T"),1000,replace = TRUE)
x

# Question 2:
# (a):
x<-rnorm(100,0,30)
x
d<-dnorm(x,0,30)
d

# (b):
p<-pnorm(x,0,30)
p

# (c):
q<-qnorm(0.2, mean=0, sd=30)
q

# (d):
q1<-qnorm(0.5, mean=0, sd=30)
q1

# Question 3:
# (a) 
x1<-rnorm(x,0,15)
x1
y<-dnorm(x1,0,15)
plot(x1,y)
# (b):
x2<-rnorm(100,0,45)
x2
y<-dnorm(x2,0,45)
plot(x2,y)
# (c):
x3<-rnorm(100,50,45)
x3
y<-dnorm(x3,50,45)
plot(x3,y)
# (d):
x4<-rnorm(100,-50,45)
x4
y<-dnorm(x4,-50,45)
plot(x4,y)

dev.off()

# Question 4:
x<-rnorm(5000,20,5)
x
hist(x)

# Question 5:
# (a):
x<-rnorm(100,22,5)
x
y<-1-pnorm(29,22,5)
y
# (b):
z<-pnorm(17,22,5)
z
# (c):
x1<-pnorm(15,22,5)+(1-pnorm(25,22,5))
x1

# Question 6:
# (a):
sigma<-4
mu<-30
x<-1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2)))
x
# (b):
x<-dnorm(31,30,4)
x


























