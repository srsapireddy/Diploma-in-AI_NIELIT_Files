# Question 1:
x<-c(8,4,5,3)
# (a):
pie(x,col=rainbow(length(x)))
# (b):

# (c):
pie(x,col=rainbow(length(x)))
legend("topright", c("Comedy", "Action", "Romance", "Science", "Fiction"),fill=rainbow(4))

# (d):
pie(x,col=rainbow(length(x)),clockwise = TRUE)
legend("topright", c("Comedy", "Action", "Romance", "Science", "Fiction"),fill=rainbow(4))

# (e):
pie(x,col=rainbow(length(x)),clockwise = TRUE,main="Movie Preferences")
legend("topright", c("Comedy", "Action", "Romance", "Science", "Fiction"),fill=rainbow(4))

# Question 2:
barplot(x,names.arg = c("Comedy", "Action", "Romance", "Science or Fiction"),col=rainbow(4),xlab = "Movie Preference",ylab = "Type",main = "Bar chart")

# Question 3:
M<-matrix(1:12,3,4)
y <- c("1st Quarter","2nd Quarter","3rd Quarter","4th Quarter")

barplot(M,names.arg=y,xlab="Quarters",ylab="Annual Product Sales",col=rainbow(3),main="Sales chart")
legend("topleft", c("1st Quarter","2nd Quarter","3rd Quarter","4th Quarter"),fill=rainbow(4))

# Question 4:
mtcars
x<-mtcars
x

hist(mtcars$mpg)

# Question 5:
plot.new()
plot.window(xlim = c(0,20),ylim=c(0,20))

# (a):
axis(1)
axis(2)

# (b):
x<-sample(1:5,5)
y<-sample(1:5,5)
points(x,y)

# (c):
lines(x,y)

# (d):
abline(h=10)

# (e):
abline(v=10)

# Question 6:
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
plot(drugA)
lines(drugB)

# Question 7:
x<-airquality
boxplot(Temp~Month,data = x)

# Question 8:
plot(iris$Petal.Length, iris$Petal.Width)

# Question 9:
y<-iris
y
pairs(~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width,data=y)