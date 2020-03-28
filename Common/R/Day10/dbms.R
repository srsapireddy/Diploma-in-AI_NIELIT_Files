install.packages("RMySQL")
require(RMySQL)
require(dbConnect)

mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = '127.0.0.1')
dbListTables(mysqlconnection)
# Query the  tables to get all the rows.
result = dbSendQuery(mysqlconnection, "select * from students")

# Store the result in an R data frame object. n = 5 is used to fetch first 5 rows.
data.frame = fetch(result, n = 5)
data.frame 

dbSendQuery(mysqlconnection, "update students set Id=6 where name1='Mini'")
dbClearResult(result)

dbSendQuery(mysqlconnection, "delete from students where Id=4")
#dbClearResult(result)

dbSendQuery(mysqlconnection, "insert into students  values (4,'Mini')")
dbClearResult(result)