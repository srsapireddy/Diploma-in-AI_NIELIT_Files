# Question 1:
ny<-read.csv(file.choose())
ny

# (a):
plot(ny$maximum.temerature,ny$minimum.temperature)


# (b):
barplot(ny$average.temperature)
# Looking at the average teperatures we can say that new york is getting colder as the time passses.

# (c:)
max(ny$maximum.temerature)
# maximum temperature is 96.
min(ny$minimum.temperature)
# minimim temperature is -6.


# (c):

# Question 2:
b<-read.csv(file.choose())
b
# (a):
# 1. Scatter Plot
plot(b$age,b$tax,xlab = "Age",ylab = "Tax", main = "Age vs Tax")

# 2. Bar Chart:
c <- table(b$age,b$tax)
c
barplot(c, main="Price Distribution by Age and Tax", col=c("darkblue","red"))

# 3. Histogram:
PTRATIO<-b$ptratio 
hist(PTRATIO,right=FALSE,main = "PTRATIO") 

# 4. Scatter Plot Matrix:
pairs(~crim+zn+age+lstat,data = b)

# (b):
?cor
cor(b,b)
