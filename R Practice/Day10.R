# Day 10:
# Question 2:
install.packages("RMySQL")
library(RMySQL)
library(dbConnect)

mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = 'localhost')
dbListTables(mysqlconnection)

result=dbSendQuery(mysqlconnection,"select * from ai37country")
data.frame = fetch(result, n = 5)
data.frame 

# (b):
dbSendQuery(mysqlconnection,"insert into ai37country values (4,'Germany','DEM','German')")
dbSendQuery(mysqlconnection,"insert into ai37country values (5,'Australia','Dollar','English')")

# (c):
result=dbSendQuery(mysqlconnection,"select * from ai37country where language='English'")

# (d):
result=dbSendQuery(mysqlconnection,"update ai37country set country_name='UK' where country_name='UK'")

# (e):
result=dbSendQuery(mysqlconnection,"delete from ai37country where country_id=1");
data.frame = fetch(result, n = 5)
data.frame 

# Question 3:
dbWriteTable(mysqlconnection, "ai37mtcars", mtcars )
result=dbSendQuery(mysqlconnection,"select * from ai37mtcars")
data.frame = fetch(result)
data.frame 

# (a):
mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = 'localhost')
result=dbSendQuery(mysqlconnection,"select * from ai37mtcars where row_names like 'Merc%' ")
data.frame = fetch(result)
data.frame 

# (b):
mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = 'localhost')
result=dbSendQuery(mysqlconnection,"select * from ai37mtcars where cyl=8")
data.frame = fetch(result)
data.frame

# (c):
mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = 'localhost')
result=dbSendQuery(mysqlconnection,"select * from ai37mtcars where hp>100")
data.frame = fetch(result)
data.frame 

#(d):
result=dbSendQuery(mysqlconnection,"select cyl,count(*) from ai37mtcars group by cyl")
data.frame = fetch(result)
data.frame 

# (e):
mysqlconnection = dbConnect(MySQL(), user = 'sw800', password = 'nielit', dbname = 'sw800', host = 'localhost')
result=dbSendQuery(mysqlconnection,"select count(*) from ai37mtcars where disp between 100 and 200")
data.frame = fetch(result)
data.frame 

# 4:
result=dbSendQuery(mysqlconnection,"select * from ai37country")
data.frame = fetch(result)
data.frame 

dbClearResult(result)