# Day 1:
# Question 3:
install.packages("caret")
install.packages("e1071")
library(caret)
library(e1071)
dataset <- read.table(file.choose())

validation_index <- createDataPartition(dataset$V9, p=0.80, list=FALSE)

# select 20% of the data for validation
validation <- dataset[-validation_index,]
# use the remaining 80% of data to training and testing the models
dataset <- dataset[validation_index,]

dim(dataset)

fit.knn <- train(V9~., data=dataset, method="knn", metric="accuracy")

predictions <- predict(fit.knn, validation)
predictions
confusionMatrix(predictions, validation$V9)
