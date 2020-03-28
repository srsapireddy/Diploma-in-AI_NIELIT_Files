install.packages("caret")
install.packages("e1071")
library(caret)
library(e1071)
dataset <- iris

validation_index <- createDataPartition(dataset$Species, p=0.80, list=FALSE)

# select 20% of the data for validation
validation <- dataset[-validation_index,]
# use the remaining 80% of data to training and testing the models
dataset <- dataset[validation_index,]

dim(dataset)

fit.knn <- train(Species~., data=dataset, method="knn", metric="accuracy")

predictions <- predict(fit.knn, validation)
predictions
confusionMatrix(predictions, validation$Species)




