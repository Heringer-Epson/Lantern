library("readr")
library("ggfortify")
source("preprocess_data.R")


fpath = './../data/LIBOR_1m_USD.csv'
#aux = run_preprocessing(fpath, '2012/2014-09')
aux = run_preprocessing(fpath, '2012/2014')

M_1 = aux['d1']$d1
M_25 = aux['d25']$d25
print(typeof(aux['d25']))
#print(M_25$y)

png(filename="./../OUTPUTS/IR.png",width=12,height=10,units="in",res=150)
par(mfrow=c(2,1), mai = c(1.2, 1.2, 0.6, 0.6))

#Top panel.
par(mai=c(0.1, 1.2, 0.6, 0.6))
plot(index(M_1), M_1$y_increm, type='l', col='blue', ylim=c(-.75,.75),
     lwd=2, xlab='', cex.lab=2, cex.axis=2, cex.main=2, xaxt='n',
     ylab='IR increment', main="IR - USD 1-month tenor")
lines(index(M_25), M_25$y_increm, type='l', col='red', ylim=c(-.75,.75), lwd=2)
legend("topleft", c("1 day", "25 day"), lty = c(1,1), col = c('blue', 'red'),
       lwd =3, cex=2)

#plot(index(M_1), M_1$y_increm)

#Bottom panel
par(mai=c(1.2, 1.2, 0.1, 0.6))

plot(index(M_1), M_1$y, type='l', col='blue', lwd=2, xlab='Time', cex.lab=2,
     cex.axis=2, ylab='IR increment')
lines(index(M_25), M_25$y, type='l', col='red', lwd=2)


#plot.xts(M_25$y_increm, lwd=3, lty=1, col='red', cex=1, ylab='AAAAAA')
#plot.xts(M_25$y, lwd=3, lty=2, col='blue', on=NA)



dev.off()


#X11()
#message("Press Return To Continue")
#invisible(readLines("stdin", n=1))
