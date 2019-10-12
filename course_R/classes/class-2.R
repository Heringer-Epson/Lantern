#R scripts for the second class.
x = seq(1,10)

#Functions
a_mean = function(x) sum(x)/length(x)
#print(a_mean(x))

#Find about accepted arguments.
args(plot.default)

a_mean_fancy = function(x, pr=2, verbose=T) {
    r = round(sum(x) / length(x), pr)
    stdE = round(sd(x)/sqrt(length(x)), pr)
    if (verbose)
        cat('Average of x is ', r, '\n')
        cat('Standard Error of x is ', stdE, '\n')
    return(list(Mean=r, stdE=stdE))
}

#print(a_mean_fancy(x, TRUE))

#Generate sample of random numbers according to gaussian distr.
z = rnorm(100,10,2)
#print(z)
#hist(z)

#out = a_mean_fancy(z, pr=4, TRUE)
#print(out$Mean)
#print(out$stdE)

#Random distributions:

r1 = runif(10, 1, 12)
#print(r1)

#Loops
#y = 12345
#x = y/2
#k = 0
#repeat{
#    k = k + 1
#    x = (x + y/x)/2
#    if (abs(x*x -y) < 1.e-4) break
#}

#print(x - sqrt(y))

n_max = 20 #max number of iterations.
y = 12345
x = array(0,20)
k = 1
x[k] = y/2
repeat{
    k = k + 1
    x[k] = (x[k-1] + y/x[k-1])/2
    if ((abs(x*x -y) < 1.e-4) | (k>n_max )) break
}

#print(x)
#print(length(x))
plot(x[1:k])
plot()
