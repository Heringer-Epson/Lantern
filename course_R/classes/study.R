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

library(ISwR)
summary(IgM)

par(mfrow=c(1,2))
boxplot(IgM, ylab='IgM', cex.bal=1.5)
log_IgM = log(IgM)
boxplot(log_IgM, ylab='log IgM', cex.lab=1.5)

#Histograms
par(mfrow=c(1,2))
hist(IgM, freq=F, xlab='IgM', cex.lab=1.5)
legend(legend=c('LogNormal distr.'), 'topright', lty=c(1), lwd=c(2), col='red')
usr1=par('usr')

hist(log_IgM, freq=F, xlab='log(IgM)', cex.lab=1.5, ylim=c(0, 0.9), main='Histogram of log(IgM)')
legend(legend=c('Normal distr.'), 'topright', lty=c(1), lwd=c(2), col='red')

mu = mean(log_IgM)
sigma = sd(log_IgM)
yrange = seq(min(log_IgM), max(log_IgM), 0.01)
points(yrange, dnorm(yrange, mu, sigma), type='l', col='red', lwd=2)

#Go back to first subplot.
par(mfg=c(1,1), usr=usr1)
xrange = seq(min(IgM), max(IgM), 0.01)
points(xrange, dlnorm(xrange, mu, sigma), type='l', col='red', lwd=2)


#Q-Q plots.
par(mfrow=c(1,2))
qqnorm(IgM)
qqnorm(log_IgM)
qrange = seq(-3,3, 0.1)
points(qrange, sigma*qrange+mu, type='l', col='red', lwd=2)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Lectures 8
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
rm(list=ls())

methods('plot')
getS3method('plot', 'histogram')

#install.packages('fitdistrplus')
library('fitdistrplus')

data('groundbeef', package='fitdistrplus')
str(groundbeef)

serv = groundbeef$serving

#Plot histogram and CDF
plotdist(serv, histo=T, demp=T)

#Cullen and Frey (Kurtosis vs square of skewness) graph
descdist(serv, boot=1000)


#Fit weibull distribution to the data.
fw = fitdist(serv, 'weibull')
class(fw)
summary(fw)

#Fit other distributions
fg = fitdist(serv, 'gamma')
fln = fitdist(serv, 'lnorm')

par(mfrow=c(2,2))
plot.legend <- c('Weibull', 'logNormal', 'gamma')
denscomp(list(fw, fln, fg), legendtext=plot.legend)
qqcomp(list(fw, fln, fg), legendtext=plot.legend)
cdfcomp(list(fw, fln, fg), legendtext=plot.legend)
ppcomp(list(fw, fln, fg), legendtext=plot.legend)

#Different data.
data('endosulfan', package='fitdistrplus')
ATV <- endosulfan$ATV
fendo.ln <- fitdist(ATV, 'lnorm')

#install.packages('actuar')
library('actuar')
fendo.ll <- fitdist(ATV, 'llogis', start=list(shape=1, scale=500))
fendo.P <- fitdist(ATV, 'pareto', start=list(shape=1, scale=500))
fendo.B <- fitdist(ATV, 'burr', start=list(shape1=0.3, shape2=1, rate=1))

cdfcomp(list(fendo.ln, fendo.ll, fendo.P, fendo.B), lwd=2, xlogscale=T,
        ylogscale=T, legendtext=c('logNormal', 'loglogistic', 'Pareto', 'Burr'))
quantile(fendo.B, probs=0.05)
quantile(ATV, probs=0.5)
gofstat(list(fendo.ln, fendo.ll, fendo.P, fendo.B),
        fitnames=c('lnorm', 'llogis', 'Pareto', 'Burr'))

rm(list=ls())

#Bootstraping.
n=100
x = rnorm(n, 5, 1)

mu=mean(x)
cat('Sample mean, mu=', mu, '\n', sep='')
cat('Theoretical standard error of mu=', sd(x)/sqrt(n), '\n', sep='')

NumIters=1000
MeanEst = array(0, NumIters)

for (i in 1:NumIters){
  MeanEst[i] = mean(sample(x, replace=T))
}
cat('Bootstrapped Standard Error of mu=', sd(MeanEst), '\n', sep='')

hist(MeanEst, freq=F)
xrange = seq(min(MeanEst), max(MeanEst), 0.01)
points(xrange, dnorm(xrange, mu, sd(x)/sqrt(n)), type='l', lwd=2, col='red')
