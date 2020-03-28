# Day 2:
# Question 1:
# (a)
y <- 1:20
y
x <- 19:1
x
z <- c(y,x)
z

# (b)
x <- c(4,6,3)
x

# Question 2:
# (a)
?rep
rep(c(4,6,3),times = 10)
# (b)
rep(c(4,6,3),times = 11,length.out=31)
# (c)
rep.int(c(4,6,3),times=c(10,20,30))

# Question 3:
# (a)
V <- c(1/3*3.14*2.27*2.27*8.28,1/3*3.14*1.98*1.98*8.04,1/3*3.14*1.69*1.69*9.06,1/3*3.14*1.88*1.88*8.70,1/3*3.14*1.64*1.64*7.58,1/3*3.14*2.14*2.14*8.34)
V

R <- c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
H <- c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
V <- 1/3*pi*R*R*H
V

# (b)
r <- round(V,2)
r

# (c)
min <- min(V)
min
max <- max(V)
max

# Question 4:
# A
A <- sample(0:999,250)
A
# B
B <- A[which(A>900)]
B
# C
C <- sort(B)
C

# Question 5:
# a
H <- c(180, 165, 160, 193)
W <- c(87, 58, 65, 100)
X <- W / (H/100 * H/100)
X

# b
b <- X[which(X>25)]
b

# c
c <- mean(X)
c

# Question 6:
# (a)
M <- c(21,42,43,44,45,46,47,48,49,50)
p1 <- mean(M)
p1
# (b)
p2 <- median(M)
p2

# Question 7:
dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry) 
sort(dry)
median(dry)
sd(dry)
var(dry)
sd(dry)^2
min(dry)
max(dry)
summary(dry)

# Question 8:
N <- sample(1:20,10, replace=TRUE)
N
E <- N[which(N %% 2 == 0)]
E













