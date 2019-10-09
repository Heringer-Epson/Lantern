#R scripts for the third class. Dataframes!


#Install sys package!
#install.packages("sys.time", repos = "http://cran.us.r-project.org")

#Working with time.
a = Sys.time()
starttime = Sys.time()
endtime = Sys.time()
#print(difftime(endtime, starttime, units="sec"))
#Lookup profilers in R. Profvis. Show example between list, array and wrapper.

#Read a dataframe
worms = read.csv('./data/worms.csv', stringsAsFactors=F)
#print(worms)
#print(class(worms))
#print(names(worms))
#print(colnames(worms))
#print(rownames(worms))
#print(worms$Area)
#print(class(worms$Area))
#print(head(worms))
#print(worms[,1:3])
#print(worms[5:15,])
#attach(worms)
#print(worms[worms$Area>3 & worms$Slope<3,])
#print(class(worms$Slope))

#Ordering
#print(worms[order(worms$Area,decreasing=T),])

#print(summary(worms))
#with(worms,tapply(worms$Worm.density,worms$Vegetation,mean))
#with(worms,tapply(worms$Worm.density,worms$Vegetation,median))

nums = sapply(worms,is.numeric)
#print(nums)
#print(worms[nums])
#print(list(worms$Vegetation))
aggregate(worms[,nums],list(worms$Vegetation),median)
aggregate(worms[,nums],list(worms$Vegetation=="Orchard"),median)
#help(aggregate)
