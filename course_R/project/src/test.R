library("xts")

fpath = './../data/LIBOR_1m_USD.csv'
M = read.csv(fpath)

a = xts(M, order.by = as.Date(rownames(M), "%Y-%m-%d"))


print(a)
