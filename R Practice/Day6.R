# Correlation and Regression

# Question 1:
x<-c(2,3,5,7,8)
y<-c(14,20,32,42,44)

# (a):
r<-lm(y~x)
r
# (b):
p<-predict(r,data.frame(x=7))
p
# (c):
abline(lm(y~x))
# (d):
plot(x,y)

# Question 2:
x<-c(8,7,6,4,2,1)
y<-c(15,19,25,23,34,40)

# (a):
cor(x,y)

# (b):
r<-lm(x~y)
r
p<-predict(r,data.frame(y=2))
p

# (c)
r<-lm(y~x)
r
p<-predict(r,data.frame(x=5))
p

# Question 3:
m<-c(6,4,8,5,3.5)
c<-c(6.5,4.5,7,5,4)
r<-lm(c~m)
r
p<-predict(r,data.frame(m=7.5))
p


# (4):
X<-c(186,189,190,192,193,193,198,201,203,205)
Y<-c(85,85,86,90,87,91,93,103,100,101)

# (a):
r<-lm(Y~X)
r
# (b):
cor(X,Y)
# (c):
r<-lm(X~Y)
r
p<-predict(r,data.frame(Y=208))
p

# (5):
X<-c(80, 79, 83, 84, 78, 60, 82, 85, 79, 84, 80, 62)
Y<-c(300, 302, 315, 330, 300, 250, 300, 340, 315, 330, 310, 240)

r<-lm(X~Y)
r

cor(X,Y)

cor.test(X,Y)
?cor

# Question 6:
x<-c(6, 7, 8, 9, 10)
y<-c(4, 3, 3, 2, 1)

# (a):
cor(x,y)

# (b):
r6<-lm(y~x)
r6

# (c):
p<-predict(r6,data.frame(x=8))
p

# Question 7:
x<-c(25, 42, 33, 54, 29, 36)
y<-c(42, 72, 50, 90, 45, 48)

r8<-lm(y~x)
r8

cor(x,y)

P<-predict(r8,data.frame(x=47))
P
