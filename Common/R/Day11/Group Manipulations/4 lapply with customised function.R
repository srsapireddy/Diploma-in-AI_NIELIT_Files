family1 <- list(name="Jones",numofchild=2,ages=c(5,7),measles=c("Y","N"))
lapply(family1, class)


#Applying customized function 
simplefunc <- function(x) {
  mytype <- class(x)
  return(mytype)
}
lapply(family1, simplefunc)




#Function is assigned Anonymously. toupper function
simplefunc <- function(x) {
  mytype <- toupper(x)
  return(mytype)
}
lapply(family1, simplefunc)
