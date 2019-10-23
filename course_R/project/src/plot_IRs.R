library("readr")
library("ggfortify")
source("preprocess_data.R")


fpath = './../data/LIBOR_1m_USD.csv'
aux = run_preprocessing(fpath, '2012/2013-09')

M_1 = aux['1d']
M_25 = aux['25d']
print(M_25)

#X11()
#autoplot(M_25$y)
#plot(M[[1]], M[[2]], col='black')
#lines(M[[1]], M$y_smoothed, col='red')
#message("Press Return To Continue")
#invisible(readLines("stdin", n=1))
