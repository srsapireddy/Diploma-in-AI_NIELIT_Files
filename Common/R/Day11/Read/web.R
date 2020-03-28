install.packages("XML")

require(XML)

input=readHTMLTable(file.choose(),which=1,stringAsFactors=FALSE)
input=readHTMLTable(file.choose(),which=2,stringAsFactors=FALSE)
input=readHTMLTable(file.choose(),which=2,stringAsFactors=FALSE,header=FALSE)
