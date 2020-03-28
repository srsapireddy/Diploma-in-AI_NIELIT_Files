#Apply

M<-matrix(1,nrow=4,ncol=3)
apply(M,1,sum)  # to get row sum   
apply(M,2,sum)  # to get column sum  / colSums



x <- cbind(x1 = 3, x2 = c(1:8))
#obtain the row means
apply(x, 1, mean)
#obtain the column means
apply(x, 2, mean)

#obtain the row sum
row.sums <- apply(x, 1, sum)
#obtain the column sum
col.sums <- apply(x, 2, sum)


N=rbind(cbind(x, Rtot = row.sums), Ctot = c(col.sums, sum(col.sums)))
N

#Applying apply to an Array

A<-array(1,c(2,3,4))
apply(A, 1, sum)
apply(A, 2, sum)
apply(A, 3, sum)

---------------------------

#lapply

x <- list(a = 1:10, b = 10:20, c=100:120)
lapply(x, mean)



thelist<-list(A=matrix(1:9,3),B=1:4,C=matrix(1:9,2),D=21)
lapply(thelist,mean)

seq(20)
i39 <- lapply(3:9, seq) 

 



x <- list(a = 1:10, beta = exp(-3:3), logic = c(TRUE,FALSE,FALSE,TRUE))
lapply(x,mean)


 

x <- list(a = 1:10, beta = exp(-3:3), logic = c(TRUE,FALSE,FALSE,TRUE), data=c("a","b","c"))
lapply(x,mean)
#sapply

thelist<-list(A=matrix(1:9,3),B=1.4,C=matrix(1:10,2),D=21)
s=sapply(thelist,sum)




















