#R scripts for the foruth class. Dataframes!

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Read the data
fpath = './data/fertyield.csv'
yields = read.csv(fpath)

#Make columns readily callable variables.
attach(yields)

#Some basic inspection of the data.
#unique(treatment)
#table(treatment)

#Get the index of the mispelled nitogen treatment. Fix it.
which(treatment == 'nitogen')
treatment[11] = 'nitrogen'
#table(treatment)

detach(yields)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

fpath = './data/scatter.csv'
data = read.csv(fpath)
attach(data)

#head(data)
#png('./OUTPUTS/test.png')
#plot(x, y, pch=23, bg='red', col='black', cex=0.5)
#dev.off()

detach(data)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

fpath = './data/weather.data.csv'
data = read.csv(fpath)
attach(data)
#head(data)

#png('./OUTPUTS/test.png')

#plot(upper)
#plot(factor(month), upper)
#plot(month, upper)

#data[which(month==6 & upper==0), 'upper'] = NA
#print(data[is.na('upper')])
detach(data)
#dev.off()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

png('./OUTPUTS/test.png')

fpath = './data/coplot.csv'
data = read.csv(fpath)
attach(data)
#head(data)

#Create separete plotitng window.
##windows(7,4) #not working.

#Create to scatter plots.
#par(mfrow=c(1,2))
#plot(x,y)
#plot(z,y)

#coplot(y~z|x,pch=16,panel=panel.smooth)
detach(data)

dev.off()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

rm(list=ls())
png('./OUTPUTS/test.png')

fpath = './data/np.csv'
data = read.csv(fpath)
attach(data)
summary(data)

#par(mfrow=c(1,2))
#plot(nitrogen,yield)
#plot(phosphorus,yield)

#Get the effect of using both phosp and nitrogen.
R = tapply(yield, list(nitrogen, phosphorus), mean)
#R is a matrix.
print(R)

barplot(R, beside=T, xlab='phosphorus')
legend('topleft', legend=c('no', 'yes'), title='nitrogen',
        fill=c('black', 'lightgrey'))

detach(data)
dev.off()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

