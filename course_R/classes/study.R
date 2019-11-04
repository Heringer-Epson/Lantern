#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 1/2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())

#Sequences and plotting.
x = seq(-1,12, 0.1)
y = x^2
plot(x,y)

#Factors.
pain = c(0,3,2,2,1)
fpain = factor(pain, levels=0:3)
levels(fpain) = c('none', 'mild', 'medium', 'severe')

as.character(fpain)
as.numeric(fpain)

fpain_ordered = ordered(fpain, c('none', 'mild', 'medium', 'severe'))
fpain_ordered[fpain_ordered >= 'medium']

#Factors. II.
fruits = sample(c('apples', 'grapes', 'oranges'), 20, replace=T, prob=c(0.5, 0.25, 0.25))
fruits_ordered = ordered(fruits, c('apples', 'oranges', 'grapes'))
fruits_ordered[fruits_ordered>'apples']

#Lists.
L = list(col_a = seq(1,10,2))
L$col_a

#For loop.
x = seq(0,1, 0.01)
plot(x,x, type='l')
for (j in seq(1,5,2)){
  points(x, x^j, type='l', col=j)
}
legend('bottomright', c('x^1', 'x^3', 'x^5'), seq(1,5,2), lty=c(4,1), cex=0.8)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 3
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())

#If in Rstudio, File path has to be set with respect to the set work directory.
worms = read.csv('./data/worms.csv')
summary(worms)

#Show columns in the data.
names(worms)
colnames(worms)

#show head of the dataframe
head(worms)

#Slicing dataframe.
worms[1:5,2:3]

#If attach is called, column names become variables.
attach(worms)
Area

#Select rows based on condition.
worms[worms$Area>2 & Slope<3,]

#Order dataframe.
head(worms[rev(order(worms$Area)),])

#tapply.
#Calculate the mean number of worms for different vegetations.
with(worms, tapply(X=worms$Worm.density, FUN=mean, INDEX=worms$Vegetation))

#sapply
#Calculate the mean for all numeric columns according to vegetation.
nums = sapply(worms, is.numeric)
nums
head(worms[nums])
aggregate(worms[nums], list(worms$Vegetation), mean)
aggregate(worms[nums], list(worms$Vegetation=='Orchard'), sd)

#Cleaning data.
yields = read.csv('./data/fertyield.csv')
attach(yields)
head(yields)
unique(treatment) #The treatment variable has been attached as a column in yields.
which(treatment=='nitogen')
treatment[11] = 'nitrogen'

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 4
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())

#Using coplot.
data = read.csv('./data/coplot.csv')
attach(data)
head(data)
coplot(y~z|x, pch=16, panel=panel.smooth)
help(coplot)

#Interactions between categorical variables.
rm(list=ls())
data = read.csv('./data/np.csv')
attach(data)
head(data)
par(mfrow=c(1,2))  
plot(nitrogen, yield, main='Nitrogen effect on yield')
plot(phosphorus, yield, main='Phosphorus effect on yield')

#Interaction plot.
R = tapply(yield, list(nitrogen, phosphorus), mean)
class(R)
R

#Careful with labels and plot order.
barplot(R, beside=T, xlab='phosphorus')
legend('topleft', legend=c('no', 'yes'), title='notrigen', fill=c('black', 'lightgrey'))

#Histograms.
rm(list=ls())
yvals = read.csv('./data/yvalues.csv')
attach(yvals)
#freq=F shows a normalized histogram.
hist(y, freq=F)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 5 and 6 were theoretical
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 7
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 8
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())
