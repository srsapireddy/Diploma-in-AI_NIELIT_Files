# Day 1:
# Question 4:
install.packages("caret")
install.packages("e1071")
library(caret)
library(e1071)
dataset <- read.csv(file.choose())

validation_index <- createDataPartition(dataset$Type, p=0.80, list=FALSE)

# select 20% of the data for validation
validation <- dataset[-validation_index,]
# use the remaining 80% of data to training and testing the models
dataset <- dataset[validation_index,]

dim(dataset)

fit.knn <- train(Type~., data=dataset, method="knn", metric="accuracy")

predictions <- predict(fit.knn, validation)
predictions
confusionMatrix(as.integer(predictions),validation$Type)


