library(caret)
library(e1071)
dataset<-iris
v<-createDataPartition(dataset$Species,p=0.8,list=FALSE)
trainset<-dataset[v,]
testset<-dataset[-v,]

fit.lda<-train(Species~.,data=trainset,method="lda",metric="Accuracy")
predictions<-predict(fit.lda,testset)
confusionMatrix(predictions,testset$Species)
class(testset)
head(testset)
predict(fit.lda,data.frame(Sepal.Length=5,Sepal.Width=4,Petal.Length=1.5,Petal.Width=0.2))


metric="Accuracy"

fit.cart <- train(Species~., data=dataset, method="rpart", metric=metric)
# kNN

fit.knn <- train(Species~., data=dataset, method="knn", metric=metric)
# c) advanced algorithms
# SVM

fit.svm <- train(Species~., data=dataset, method="svmRadial", metric=metric)
# Random Forest

fit.rf <- train(Species~., data=dataset, method="rf", metric=metric)


predictions<-predict(fit.knn,testset)
confusionMatrix(predictions,testset$Species)
