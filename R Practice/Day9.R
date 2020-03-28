# Day 9
# Question 1:
# (a):
x1<-dbinom(5,50,0.8)
x1

# (b):
x2<-dbinom(5,50,0.05)
x2

# (c):
x3<-dbinom(5,50,0.8)
x3

# (d):
x4<-1-dbinom(25,50,0.8)
x4

# (e)
x5<-dbinom(5,50,0.05)
x5

# Question 2:
# (a):
x1<-dbinom(40,60,0.65)
x1

x2<-1-dbinom(40,60,0.65)
x2

# Question 3:
# (a):
x<- seq(0,30, 1)
x
y<-dbinom(x,30,0.15)
y
plot(x,y)

# (b)
x<- seq(0,30, 1)
x
y<-dbinom(x,30,0.4)
y
plot(x,y)

# (c):
x<- seq(0,30, 1)
x
y<-dbinom(x,30,0.8)
y
plot(x,y)

# Question 4:
# (a):
pbinom(20,60,0.5)
pbinom(25,60,0.5)
pbinom(30,60,0.5)

sum(dbinom(c(20,25,30),60,prob=0.5))

# (b):
pbinom(19,60,prob=0.5)

# (c):
pbinom(30,60,prob=0.5)-pbinom(20,60,prob=0.5)

# Question 5:
dpois(100,5)
dpois(100,25)
dpois(100,50)
?dpois

# Question 6:
x<-rpois(2608,(10097/2608))
x
hist(x)
?rpois

# Question 7:
# (a):
ppois(5,7)
ppois(4,7) 

# (b):
1-ppois(10,7)

# (c):
ppois(16,7)-ppois(3,7) 

# Question 8:
?runif
x<-dunif(6,1,25)
x
