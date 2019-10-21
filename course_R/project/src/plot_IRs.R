library("readr")
source("preprocess_data.R")


fpath = './../data/LIBOR_1m_USD.csv'
M = run_preprocessing(fpath)

#X11()
#plot(M[[1]], M[[2]], col='black')
#lines(M[[1]], M$y_smoothed, col='red')
#message("Press Return To Continue")
#invisible(readLines("stdin", n=1))
