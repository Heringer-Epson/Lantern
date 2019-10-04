#R script for the second class.

#Just some test to familiarize ourselvess with R functions.
A = seq(-10,10,2)
#print(A)
#print(paste('Modulo operation', 10 %% 3))
#print(paste('Interger of division', 10 %/% 3))

#Indexing.
#print(A[1:3])

#Define matrix using arrays.
B = array(0, 10) #1D
#print(B)

C = array(0, c(10,2))
#print(C)

D = array(seq(1,20), c(10,2))
#print(D)

#Lists! c function
a = c(1, 2, 4, 8)
#print(a)

b = c("1", "2", "3", "7")
#print(a)
#print(as.character(a))
#print(as.numeric(b))

#Lists!
s = list(a, b)
#print(s)
#print(s[[2]][1])

#Name list components. Seems like a python dictionary.
L = list(NumericVector=a, StringVector=b)
#print(L)
#print(L$NumericVector)
#print(L$NumericVector[3])

#factors.
pain = c(0, 3, 2, 2, 1)
fpain = factor(pain, levels=0:3)
levels(fpain) = c('none', 'mild', 'medium', 'severe')
#print(fpain)
#print(as.character(fpain))
#print(as.numeric(fpain))

#Cardinal factors
fpain = ordered(fpain, c('none', 'mild', 'medium', 'severe'))
#print((fpain >= "medium"))

#another example.
fruits = sample(c("apples", "oranges", "grapes"), 20, replace=TRUE,
                prob=c(00.5, 0.25, 0.25))
print(fruits)
#class(fruits)
#fruits = ordered(fruits, c('apples', 'oranges', 'grapes')
